from contextlib import contextmanager

import allure
from playwright.sync_api import Error, Locator, TimeoutError, expect

from config.test_data import PresentUiElementExpectation, VisibleUiElementExpectation
from config.settings import settings
from helpers.locators import get_by_class, get_by_css
from helpers.ui_helper import UiHelper


class BasePage:
    path = ""

    def __init__(self, helper: UiHelper):
        self.helper = helper

    def open(self) -> None:
        self.helper.open_path(self.path)

    def wait_for_path(self, path: str) -> None:
        self.helper.wait_for_path(path)

    def wait_for_any_path(self, paths: list[str]) -> None:
        self.helper.wait_for_any_path(paths)

    def expect_visible(self, locator: Locator) -> None:
        expect(locator).to_be_visible(timeout=settings.timeout)

    def scroll_to(self, locator: Locator) -> None:
        self.helper.element.scroll_to(locator)

    def _get_element_locator(self, selector_type: str, selector_value: str, element_name: str):
        selector_map = {
            "class": lambda: get_by_class(self.helper, selector_value),
            "css": lambda: get_by_css(self.helper, selector_value),}
        locator_factory = selector_map.get(selector_type)
        if locator_factory is None:
            raise ValueError(
                f"Unsupported selector_type '{selector_type}' for {element_name}.")
        return locator_factory()

    def should_have_visible_ui_element(self, element: VisibleUiElementExpectation) -> None:
        with self.step(f"Verify visible UI element '{element.name}'"):
            locator = self._get_element_locator(
                element.selector_type,
                element.selector_value,
                element.name,)
            expect(locator.first).to_be_visible(timeout=settings.timeout)
            actual_count = locator.count()
            assert actual_count >= element.minimum_count, (
                f"{element.name} expected at least {element.minimum_count} elements for "
                f"selector '{element.selector_value}', but found {actual_count}.")
            visible_elements = [
                locator.nth(index).is_visible()
                for index in range(actual_count)]
            assert any(visible_elements), (
                f"{element.name} found {actual_count} element(s) for selector "
                f"'{element.selector_value}', but none are visible.")

    def should_have_present_ui_element(self, element: PresentUiElementExpectation) -> None:
        with self.step(f"Verify UI element exists in DOM '{element.name}'"):
            locator = self._get_element_locator(
                element.selector_type,
                element.selector_value,
                element.name,)
            actual_count = locator.count()
            assert actual_count >= element.minimum_count, (
                f"{element.name} expected at least {element.minimum_count} elements for "
                f"selector '{element.selector_value}', but found {actual_count}.")

    def attach_failure_screenshot(self, name: str) -> None:
        try:
            allure.attach(
                self.helper.page.screenshot(full_page=True, timeout=settings.timeout),
                name=name,
                attachment_type=allure.attachment_type.PNG,)
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
