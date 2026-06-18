from __future__ import annotations

from typing import TYPE_CHECKING

from playwright.sync_api import Locator

if TYPE_CHECKING:
    from helpers.ui_helper import UiHelper


LOGIN_SOCIAL_ICONS_CLASS = "oxd-icon orangehrm-sm-icon"
LOGIN_BRANDING_CONTAINER_CLASS = "orangehrm-login-branding"
LOGIN_BRANDING_LOGO_CSS = 'img[alt="orangehrm-logo"]'
RESET_PASSWORD_REQUIRED_MESSAGE_CSS = (
    "#app > div.orangehrm-forgot-password-container > "
    "div.orangehrm-forgot-password-wrapper > div > form > "
    "div.oxd-form-row > div > span"
)
RESET_PASSWORD_SUCCESS_TITLE_CSS = ".orangehrm-forgot-password-title"
SIDEBAR_CONTAINER_CLASS = "oxd-sidepanel-body"
SIDEBAR_COLLAPSE_BUTTON_CSS = (
    "button.oxd-icon-button.oxd-main-menu-button:has(i.bi-chevron-left)"
)
SIDEBAR_EXPAND_BUTTON_CSS = (
    "button.oxd-icon-button.oxd-main-menu-button:has(i.bi-chevron-right)"
)
USER_DROPDOWN_CLASS = "oxd-userdropdown"
FORGOT_PASSWORD_LINK_CLASS = "oxd-text oxd-text--p orangehrm-login-forgot-header"
RESET_PASSWORD_CARD_CONTAINER_CLASS = "orangehrm-card-container"
EMPLOYEE_DISTRIBUTION_WIDGET_CSS = (
    "div.oxd-sheet.orangehrm-dashboard-widget:has("
    ".orangehrm-dashboard-widget-name p:has-text('Employee Distribution by Sub Unit')"
    ")"
)
EMPLOYEE_DISTRIBUTION_CHART_CANVAS_CSS = (
    "div.oxd-sheet.orangehrm-dashboard-widget:has("
    ".orangehrm-dashboard-widget-name p:has-text('Employee Distribution by Sub Unit')"
    ") "
    "div.oxd-pie-chart canvas"
)
EMPLOYEE_DISTRIBUTION_CHART_TOOLTIP_CSS = ".oxd-pie-chart-tooltip"
EMPLOYEE_DISTRIBUTION_LEGEND_CSS = (
    "div.oxd-sheet.orangehrm-dashboard-widget:has("
    ".orangehrm-dashboard-widget-name p:has-text('Employee Distribution by Sub Unit')"
    ") "
    "ul.oxd-chart-legend"
)
EMPLOYEE_DISTRIBUTION_FIRST_LEGEND_ITEM_CSS = (
    "div.oxd-sheet.orangehrm-dashboard-widget:has("
    ".orangehrm-dashboard-widget-name p:has-text('Employee Distribution by Sub Unit')"
    ") "
    "ul.oxd-chart-legend li:first-child"
)
EMPLOYEE_DISTRIBUTION_FIRST_LEGEND_LABEL_CSS = (
    "div.oxd-sheet.orangehrm-dashboard-widget:has("
    ".orangehrm-dashboard-widget-name p:has-text('Employee Distribution by Sub Unit')"
    ") "
    "ul.oxd-chart-legend li:first-child span.oxd-text.oxd-text--span"
)


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


def get_employee_distribution_widget(helper: UiHelper) -> Locator:
    return get_by_css(helper, EMPLOYEE_DISTRIBUTION_WIDGET_CSS)


def get_employee_distribution_chart_canvas(helper: UiHelper) -> Locator:
    return get_by_css(helper, EMPLOYEE_DISTRIBUTION_CHART_CANVAS_CSS)


def get_employee_distribution_chart_tooltip(helper: UiHelper) -> Locator:
    return get_by_css(helper, EMPLOYEE_DISTRIBUTION_CHART_TOOLTIP_CSS)


def get_employee_distribution_legend(helper: UiHelper) -> Locator:
    return get_by_css(helper, EMPLOYEE_DISTRIBUTION_LEGEND_CSS)


def get_employee_distribution_first_legend_item(helper: UiHelper) -> Locator:
    return get_by_css(helper, EMPLOYEE_DISTRIBUTION_FIRST_LEGEND_ITEM_CSS)


def get_employee_distribution_first_legend_label(helper: UiHelper) -> Locator:
    return get_by_css(helper, EMPLOYEE_DISTRIBUTION_FIRST_LEGEND_LABEL_CSS)
