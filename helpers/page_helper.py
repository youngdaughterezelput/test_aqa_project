from playwright.sync_api import Locator, Page

from config.settings import settings


class PageHelper:
    def __init__(self, page: Page):
        self.page = page

    def open_path(self, path: str) -> None:
        self.page.goto(
            f"{settings.base_url}{path}",
            wait_until="domcontentloaded",
            timeout=settings.timeout,
        )

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

    def wait_for_url(self, url_part: str) -> None:
        self.page.wait_for_url(f"**{url_part}**", timeout=settings.timeout)

    def set_default_timeout(self) -> None:
        self.page.set_default_timeout(settings.timeout)
