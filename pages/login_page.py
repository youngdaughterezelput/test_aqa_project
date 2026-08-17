import re

from playwright.sync_api import expect
from config.settings import settings
from config.test_data import (
    LoginUser,
    PresentUiElementExpectation,
    UiElementCollection,
    VisibleUiElementExpectation,)
from helpers.locators import (
    get_forgot_password_link,
    get_invalid_credentials_alert,
    get_login_button,
    get_login_copyright_link,
    get_login_password_input,
    get_login_title,
    get_login_username_input,
    get_by_class,
)
from helpers.paths import LOGIN_PATH
from pages.base_page import BasePage


class LoginPage(BasePage):
    path = LOGIN_PATH

    def __init__(self, helper):
        super().__init__(helper)
        self.username_input = get_login_username_input(helper)
        self.password_input = get_login_password_input(helper)
        self.login_button = get_login_button(helper)
        self.invalid_credentials_alert = get_invalid_credentials_alert(helper)
        self.login_title = get_login_title(helper)
        self.forgot_password_link = get_forgot_password_link(helper)
        self.copyright_link = get_login_copyright_link(helper)

    def open(self) -> None:
        with self.step("Open login page"):
            super().open()
            expect(self.username_input).to_be_visible(timeout=settings.timeout)

    def login(self, user: LoginUser) -> None:
        with self.step(f"Login as user '{user.username}'"):
            self.username_input.fill(user.username)
            self.password_input.fill(user.password)
            self.login_button.click()

    def should_have_invalid_credentials_error(self) -> None:
        with self.step("Verify invalid credentials error is displayed"):
            expect(self.invalid_credentials_alert).to_be_visible(timeout=settings.timeout)

    def click_forgot_password(self) -> None:
        with self.step("Click forgot password link"):
            self.forgot_password_link.click()

    def should_have_copyright_link(self) -> None:
        with self.step("Verify copyright text contains a link"):
            expect(self.copyright_link).to_be_visible(timeout=settings.timeout)
            expect(self.copyright_link).to_have_attribute(
                "href",
                re.compile(r"^https?://.+"),
                timeout=settings.timeout,)

    def should_have_ui_element_collection(self, collection: UiElementCollection) -> None:
        with self.step(f"Verify UI collection '{collection.name}'"):
            elements = get_by_class(self.helper, collection.class_name)
            actual_count = elements.count()
            assert actual_count >= collection.minimum_count, (
                f"{collection.name} expected at least {collection.minimum_count} elements "
                f"with class '{collection.class_name}', but found {actual_count}.")
            for index in range(actual_count):
                expect(elements.nth(index)).to_be_visible(timeout=settings.timeout)
