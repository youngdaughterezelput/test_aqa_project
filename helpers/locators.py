from playwright.sync_api import Locator

from helpers.ui_helper import UiHelper


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
