from config.settings import settings
from helpers.locators import (
    get_header_container,
    get_header_upgrade_button,
    get_header_user_menu,
    get_header_user_menu_trigger,
)


class HeaderComponent:
    def __init__(self, helper):
        self.container = get_header_container(helper)
        self.upgrade_button = get_header_upgrade_button(helper)
        self.user_menu_trigger = get_header_user_menu_trigger(helper)
        self.user_menu = get_header_user_menu(helper)

    def open_user_menu(self) -> None:
        self.user_menu_trigger.click(timeout=settings.timeout)
