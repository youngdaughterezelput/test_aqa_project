from playwright.sync_api import Locator

from config.settings import settings
from helpers.locators import (
    get_sidebar_collapse_button,
    get_sidebar_container,
    get_sidebar_expand_button,
    get_sidebar_menu,
    get_sidebar_menu_item,
    get_sidebar_menu_items,
    get_sidebar_search_input,
)


class SidebarComponent:
    def __init__(self, helper):
        self.helper = helper
        self.container = get_sidebar_container(helper)
        self.collapse_button = get_sidebar_collapse_button(helper)
        self.expand_button = get_sidebar_expand_button(helper)
        self.menu = get_sidebar_menu(helper)
        self.search_input = get_sidebar_search_input(helper)
        self.menu_items = get_sidebar_menu_items(helper)

    def menu_item(self, name: str) -> Locator:
        return get_sidebar_menu_item(self.helper, name)

    def search(self, query: str) -> None:
        self.search_input.fill(query, timeout=settings.timeout)

    def visible_menu_item_names(self) -> list[str]:
        return [
            self.menu_items.nth(index).inner_text().strip()
            for index in range(self.menu_items.count())
            if self.menu_items.nth(index).is_visible()
        ]

    def click_menu_item(self, name: str) -> None:
        self.menu_item(name).click(timeout=settings.timeout)
