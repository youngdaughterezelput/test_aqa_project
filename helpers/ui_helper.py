import re

from playwright.sync_api import Locator, Page, expect

from components.sidebar_component import SidebarComponent
from config.settings import settings


class ElementUiHelper:
    def __init__(self, helper: "UiHelper"):
        self.helper = helper

    def is_in_viewport(self, locator: Locator) -> bool:
        return locator.evaluate(
            """element => {
                const rect = element.getBoundingClientRect();
                return (
                    rect.top >= 0 &&
                    rect.left >= 0 &&
                    rect.bottom <= window.innerHeight &&
                    rect.right <= window.innerWidth
                );
            }""")

    def scroll_to(
        self,
        locator: Locator,
        *,
        max_attempts: int = 8,
        step: int = 700,) -> None:
        for _ in range(max_attempts):
            if locator.is_visible() and self.is_in_viewport(locator):
                return
            self.helper.page.mouse.wheel(0, step)
        locator.scroll_into_view_if_needed(timeout=settings.timeout)
        expect(locator).to_be_visible(timeout=settings.timeout)

    def scroll_until_visible(
        self,
        locator: Locator,
        *,
        max_attempts: int = 8,
        step: int = 700,) -> None:
        self.scroll_to(locator, max_attempts=max_attempts, step=step)

    def hover(self, locator: Locator, position: dict[str, float] | None = None) -> None:
        locator.hover(position=position, timeout=settings.timeout)

    def click(self, locator: Locator) -> None:
        locator.click(timeout=settings.timeout)

    def hover_until_visible(
        self,
        locator: Locator,
        target_locator: Locator,
        positions: list[dict[str, float]],
    ) -> None:
        for position in positions:
            self.hover(locator, position=position)
            if target_locator.count() > 0 and target_locator.first.is_visible():
                return
        expect(target_locator).to_be_visible(timeout=settings.timeout)

    def wait_until_canvas_changes(self, locator: Locator, previous_snapshot: str) -> str:
        self.helper.page.wait_for_function(
            """([canvas, previousSnapshot]) => canvas.toDataURL() !== previousSnapshot""",
            arg=[locator.element_handle(), previous_snapshot],
            timeout=settings.timeout,)
        return locator.evaluate("canvas => canvas.toDataURL()")


class SidebarUiHelper:
    def __init__(self, helper: "UiHelper"):
        self.helper = helper

    def is_open(self) -> bool:
        sidebar = SidebarComponent(self.helper)
        return sidebar.collapse_button.is_visible()

    def ensure_open(self) -> None:
        sidebar = SidebarComponent(self.helper)
        if self.is_open():
            expect(sidebar.collapse_button).to_be_visible(timeout=settings.timeout)
            return
        expect(sidebar.expand_button).to_be_visible(timeout=settings.timeout)
        sidebar.expand_button.click()
        expect(sidebar.collapse_button).to_be_visible(timeout=settings.timeout)
        expect(sidebar.expand_button).not_to_be_visible(timeout=settings.timeout)

    def collapse(self) -> None:
        sidebar = SidebarComponent(self.helper)
        self.ensure_open()
        sidebar.collapse_button.click()
        expect(sidebar.expand_button).to_be_visible(timeout=settings.timeout)
        expect(sidebar.collapse_button).not_to_be_visible(timeout=settings.timeout)


class UiHelper:
    def __init__(self, page: Page):
        self.page = page
        self.element = ElementUiHelper(self)
        self.sidebar = SidebarUiHelper(self)

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
