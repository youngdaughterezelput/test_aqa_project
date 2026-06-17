from playwright.sync_api import Locator

from helpers.page_helper import PageHelper


def get_by_placeholder(helper: PageHelper, text: str) -> Locator:
    return helper.by_placeholder(text)


def get_by_role(helper: PageHelper, role: str, name: str) -> Locator:
    return helper.by_role(role, name)


def get_by_text(helper: PageHelper, text: str) -> Locator:
    return helper.by_text(text)


def get_by_class(helper: PageHelper, class_name: str) -> Locator:
    return helper.by_class(class_name)


def get_by_css(helper: PageHelper, selector: str) -> Locator:
    return helper.by_css(selector)
