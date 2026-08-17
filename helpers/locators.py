from __future__ import annotations

from typing import TYPE_CHECKING

from playwright.sync_api import Locator

if TYPE_CHECKING:
    from helpers.ui_helper import UiHelper


LOGIN_SOCIAL_ICONS_CLASS = "oxd-icon orangehrm-sm-icon"
LOGIN_BRANDING_CONTAINER_CLASS = "orangehrm-login-branding"
LOGIN_BRANDING_LOGO_CSS = 'img[alt="orangehrm-logo"]'
LOGIN_COPYRIGHT_LINK_CSS = (
    "#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > "
    "div > div.orangehrm-login-slot > div.orangehrm-login-footer > "
    "div.orangehrm-copyright-wrapper > p:nth-child(2) > a"
)
LOGIN_FORM_CONTENT_CSS = (
    "#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > "
    "div > div.orangehrm-login-slot > div.orangehrm-login-form > div > div"
)
RESET_PASSWORD_REQUIRED_MESSAGE_CSS = (
    "#app > div.orangehrm-forgot-password-container > "
    "div.orangehrm-forgot-password-wrapper > div > form > "
    "div.oxd-form-row > div > span")
RESET_PASSWORD_SUCCESS_TITLE_CSS = ".orangehrm-forgot-password-title"
SIDEBAR_CONTAINER_CLASS = "oxd-sidepanel-body"
HEADER_CONTAINER_CSS = (
    "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > "
    "header > div.oxd-topbar-header"
)
HEADER_UPGRADE_BUTTON_CSS = (
    f"{HEADER_CONTAINER_CSS} > div.orangehrm-upgrade-container > a > button"
)
HEADER_USER_MENU_TRIGGER_CSS = (
    f"{HEADER_CONTAINER_CSS} > div.oxd-topbar-header-userarea > ul > li > span"
)
HEADER_USER_MENU_CSS = (
    f"{HEADER_CONTAINER_CSS} > div.oxd-topbar-header-userarea > ul > li > ul"
)
SIDEBAR_MENU_CSS = (
    "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > "
    "aside > nav > div.oxd-sidepanel-body > div > div"
)
SIDEBAR_SEARCH_INPUT_CSS = 'aside input[placeholder="Search"]'
SIDEBAR_MENU_ITEM_CSS = "a.oxd-main-menu-item"
SIDEBAR_COLLAPSE_BUTTON_CSS = (
    "button.oxd-icon-button.oxd-main-menu-button:has(i.bi-chevron-left)")
SIDEBAR_EXPAND_BUTTON_CSS = (
    "button.oxd-icon-button.oxd-main-menu-button:has(i.bi-chevron-right)")
USER_DROPDOWN_CLASS = "oxd-userdropdown"
FORGOT_PASSWORD_LINK_CLASS = "oxd-text oxd-text--p orangehrm-login-forgot-header"
RESET_PASSWORD_CARD_CONTAINER_CLASS = "orangehrm-card-container"
DASHBOARD_PIE_CHART_TOOLTIP_CSS = ".oxd-pie-chart-tooltip"
DASHBOARD_WIDGET_ICON_CSS = "i.oxd-icon.bi-pie-chart-fill.orangehrm-dashboard-widget-icon"
OXD_SHEET_DASHBOARD_WIDGET_CSS = "div.oxd-sheet.orangehrm-dashboard-widget"


def get_by_placeholder(helper: UiHelper, text: str) -> Locator:
    return helper.by_placeholder(text)


def get_by_role(helper: UiHelper, role: str, name: str) -> Locator:
    return helper.by_role(role, name)


def get_by_text(helper: UiHelper, text: str) -> Locator:
    return helper.by_text(text)


def get_by_class(helper: UiHelper, class_name: str) -> Locator:
    return helper.by_class(class_name)


def get_by_css(helper: UiHelper, selector: str) -> Locator:
    return helper.by_css(selector)


def get_dashboard_header(helper: UiHelper) -> Locator:
    return get_by_role(helper, "heading", "Dashboard")


def get_user_dropdown(helper: UiHelper) -> Locator:
    return get_by_class(helper, USER_DROPDOWN_CLASS)


def get_header_container(helper: UiHelper) -> Locator:
    return get_by_css(helper, HEADER_CONTAINER_CSS)


def get_header_upgrade_button(helper: UiHelper) -> Locator:
    return get_by_css(helper, HEADER_UPGRADE_BUTTON_CSS)


def get_header_user_menu_trigger(helper: UiHelper) -> Locator:
    return get_by_css(helper, HEADER_USER_MENU_TRIGGER_CSS)


def get_header_user_menu(helper: UiHelper) -> Locator:
    return get_by_css(helper, HEADER_USER_MENU_CSS)


def get_login_username_input(helper: UiHelper) -> Locator:
    return get_by_placeholder(helper, "Username")


def get_login_password_input(helper: UiHelper) -> Locator:
    return get_by_placeholder(helper, "Password")


def get_login_button(helper: UiHelper) -> Locator:
    return get_by_role(helper, "button", "Login")


def get_invalid_credentials_alert(helper: UiHelper) -> Locator:
    return get_by_text(helper, "Invalid credentials")


def get_login_title(helper: UiHelper) -> Locator:
    return get_by_role(helper, "heading", "Login")


def get_forgot_password_link(helper: UiHelper) -> Locator:
    return get_by_class(helper, FORGOT_PASSWORD_LINK_CLASS)


def get_login_copyright_link(helper: UiHelper) -> Locator:
    return get_by_css(helper, LOGIN_COPYRIGHT_LINK_CSS)


def get_login_form_content(helper: UiHelper) -> Locator:
    return get_by_css(helper, LOGIN_FORM_CONTENT_CSS)


def get_reset_password_card_container(helper: UiHelper) -> Locator:
    return get_by_class(helper, RESET_PASSWORD_CARD_CONTAINER_CLASS)


def get_reset_password_username_input(helper: UiHelper) -> Locator:
    return get_by_placeholder(helper, "Username")


def get_reset_password_button(helper: UiHelper) -> Locator:
    return get_by_role(helper, "button", "Reset Password")


def get_cancel_button(helper: UiHelper) -> Locator:
    return get_by_role(helper, "button", "Cancel")


def get_sidebar_container(helper: UiHelper) -> Locator:
    return get_by_class(helper, SIDEBAR_CONTAINER_CLASS)


def get_sidebar_collapse_button(helper: UiHelper) -> Locator:
    return get_by_css(helper, SIDEBAR_COLLAPSE_BUTTON_CSS)


def get_sidebar_expand_button(helper: UiHelper) -> Locator:
    return get_by_css(helper, SIDEBAR_EXPAND_BUTTON_CSS)


def get_sidebar_menu(helper: UiHelper) -> Locator:
    return get_by_css(helper, SIDEBAR_MENU_CSS)


def get_sidebar_search_input(helper: UiHelper) -> Locator:
    return get_by_css(helper, SIDEBAR_SEARCH_INPUT_CSS)


def get_sidebar_menu_items(helper: UiHelper) -> Locator:
    return get_by_css(helper, f"{SIDEBAR_MENU_CSS} {SIDEBAR_MENU_ITEM_CSS}")


def get_sidebar_menu_item(helper: UiHelper, name: str) -> Locator:
    return get_sidebar_menu_items(helper).filter(has_text=name)


def _dashboard_widget_css(title: str) -> str:
    return (
        f"{OXD_SHEET_DASHBOARD_WIDGET_CSS}:has("
        f".orangehrm-dashboard-widget-name p:has-text('{title}')"
        f")")


def get_dashboard_widget_root(helper: UiHelper, title: str) -> Locator:
    return get_by_css(helper, _dashboard_widget_css(title))


def get_dashboard_widget_icon(helper: UiHelper, title: str) -> Locator:
    return get_by_css(helper, f"{_dashboard_widget_css(title)} {DASHBOARD_WIDGET_ICON_CSS}")


def get_dashboard_widget_chart_canvas(helper: UiHelper, title: str) -> Locator:
    return get_by_css(helper, f"{_dashboard_widget_css(title)} div.oxd-pie-chart canvas")


def get_dashboard_widget_chart_tooltip(helper: UiHelper) -> Locator:
    return get_by_css(helper, DASHBOARD_PIE_CHART_TOOLTIP_CSS)


def get_dashboard_widget_legend(helper: UiHelper, title: str) -> Locator:
    return get_by_css(helper, f"{_dashboard_widget_css(title)} ul.oxd-chart-legend")


def get_dashboard_widget_first_legend_item(helper: UiHelper, title: str) -> Locator:
    return get_by_css(helper, f"{_dashboard_widget_css(title)} ul.oxd-chart-legend li:first-child")


def get_dashboard_widget_first_legend_label(helper: UiHelper, title: str) -> Locator:
    return get_by_css(
        helper,
        (
            f"{_dashboard_widget_css(title)} "
            "ul.oxd-chart-legend li:first-child span.oxd-text.oxd-text--span"
        ),)
