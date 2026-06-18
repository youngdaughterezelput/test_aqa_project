from helpers.locators import (
    get_sidebar_collapse_button,
    get_sidebar_container,
    get_sidebar_expand_button,
)


class SidebarComponent:
    def __init__(self, helper):
        self.container = get_sidebar_container(helper)
        self.collapse_button = get_sidebar_collapse_button(helper)
        self.expand_button = get_sidebar_expand_button(helper)
