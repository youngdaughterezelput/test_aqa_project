import re

from playwright.sync_api import Locator, Page, expect

from config.settings import settings


class UiHelper:
    def __init__(self, page: Page):
        self.page = page

    def open_path(self, path: str) -> None:
        self.page.goto(
            f"{settings.base_url}{path}",
            wait_until="domcontentloaded",
            timeout=settings.timeout,)

    def by_placeholder(self, text: str) -> Locator:
        return self.page.get_by_placeholder(text)

    def by_role(self, role: str, name: str) -> Locator:
        return self.page.get_by_role(role, name=name)

    def by_text(self, text: str) -> Locator:
        return self.page.get_by_text(text)

    def by_class(self, class_name: str) -> Locator:
        classes = ".".join(class_name.split())
        return self.page.locator(f".{classes}")

    def by_css(self, selector: str) -> Locator:
        return self.page.locator(selector)

    def has_path(self, path: str) -> bool:
        return path in self.page.url

    def wait_for_path(self, path: str) -> None:
        if self.has_path(path):
            return
        expected_url_pattern = re.compile(rf".*{re.escape(path)}$")
        expect(self.page).to_have_url(expected_url_pattern, timeout=settings.timeout)

    def wait_for_any_path(self, paths: list[str]) -> None:
        if any(self.has_path(path) for path in paths):
            return
        expected_url_pattern = re.compile(
            rf".*({'|'.join(re.escape(path) for path in paths)})$")
        expect(self.page).to_have_url(expected_url_pattern, timeout=settings.timeout)

    def set_default_timeout(self) -> None:
        self.page.set_default_timeout(settings.timeout)
        self.page.set_default_navigation_timeout(settings.timeout)
