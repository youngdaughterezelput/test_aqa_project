from contextlib import contextmanager

import allure
from playwright.sync_api import Locator, expect

from config.settings import settings
from helpers.page_helper import PageHelper


class BasePage:
    path = ""

    def __init__(self, helper: PageHelper):
        self.helper = helper

    def open(self) -> None:
        self.helper.open_path(self.path)

    def wait_for_url(self, url_part: str) -> None:
        self.helper.wait_for_url(url_part)

    def expect_visible(self, locator: Locator) -> None:
        expect(locator).to_be_visible(timeout=settings.timeout)

    @contextmanager
    def step(self, title: str):
        with allure.step(title):
            try:
                yield
            except Exception:
                allure.attach(
                    self.helper.page.screenshot(full_page=True),
                    name=f"{title} - failed",
                    attachment_type=allure.attachment_type.PNG,
                )
                raise
