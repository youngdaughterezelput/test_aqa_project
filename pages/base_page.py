from contextlib import contextmanager

import allure
from playwright.sync_api import Error, Locator, TimeoutError, expect

from config.settings import settings
from helpers.ui_helper import UiHelper


class BasePage:
    path = ""

    def __init__(self, helper: UiHelper):
        self.helper = helper

    def open(self) -> None:
        self.helper.open_path(self.path)

    def wait_for_path(self, path: str) -> None:
        self.helper.wait_for_path(path)

    def expect_visible(self, locator: Locator) -> None:
        expect(locator).to_be_visible(timeout=settings.timeout)

    def attach_failure_screenshot(self, name: str) -> None:
        try:
            allure.attach(
                self.helper.page.screenshot(full_page=True, timeout=settings.timeout),
                name=name,
                attachment_type=allure.attachment_type.PNG,
            )
        except (TimeoutError, Error):
            # Preserve the original test failure even if Playwright cannot finish the screenshot.
            pass

    @contextmanager
    def step(self, title: str):
        with allure.step(title):
            try:
                yield
            except Exception:
                self.attach_failure_screenshot(f"{title} - failed")
                raise
