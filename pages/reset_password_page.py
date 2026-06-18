from playwright.sync_api import expect

from config.settings import settings
from config.test_data import (
    ResetPasswordRequest,
    reset_password_required_message,
    reset_password_success_title,)
from helpers.locators import (
    get_cancel_button,
    get_reset_password_button,
    get_reset_password_card_container,
    get_reset_password_username_input,
)
from helpers.paths import (
    LOGIN_PATH,
    REQUEST_PASSWORD_RESET_PATH,
    REQUEST_RESET_PASSWORD_PATH,
    SEND_PASSWORD_RESET_PATH,)
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):
    path = REQUEST_PASSWORD_RESET_PATH
    confirmation_paths = [
        SEND_PASSWORD_RESET_PATH,
        REQUEST_RESET_PASSWORD_PATH,]

    def __init__(self, helper):
        super().__init__(helper)
        self.card_container = get_reset_password_card_container(helper)
        self.username_input = get_reset_password_username_input(helper)
        self.reset_password_button = get_reset_password_button(helper)
        self.cancel_button = get_cancel_button(helper)

    def should_be_opened(self) -> None:
        with self.step("Verify reset password page URL"):
            self.wait_for_path(self.path)

    def should_display_reset_password_form(self) -> None:
        with self.step("Verify reset password form is displayed"):
            self.should_be_opened()
            expect(self.username_input).to_be_visible(timeout=settings.timeout)
            expect(self.reset_password_button).to_be_visible(timeout=settings.timeout)

    def should_display_card_container(self) -> None:
        with self.step("Verify reset password card container is displayed"):
            self.should_be_opened()
            if self.card_container.count() > 0:
                visible_cards = [
                    self.card_container.nth(index).is_visible()
                    for index in range(self.card_container.count())]
                assert any(
                    visible_cards
                ), "Reset password card container is present but not visible."
                return
            raise AssertionError("Reset password card container was not found on the page.")

    def fill_username(self, request: ResetPasswordRequest) -> None:
        with self.step(f"Fill username '{request.username}' in reset password form"):
            self.username_input.fill(request.username)

    def click_reset_password(self) -> None:
        with self.step("Click reset password button"):
            self.reset_password_button.click()

    def click_cancel(self) -> None:
        with self.step("Click cancel button"):
            self.cancel_button.click()

    def submit_reset_password_request(self, request: ResetPasswordRequest) -> None:
        with self.step("Submit reset password request"):
            self.fill_username(request)
            self.click_reset_password()

    def should_redirect_to_confirmation_page(self) -> None:
        with self.step("Verify redirect to reset password confirmation page"):
            self.wait_for_any_path(self.confirmation_paths)

    def should_show_reset_password_success_title(self) -> None:
        self.should_have_visible_ui_element(reset_password_success_title)

    def should_show_required_error_for_username(self) -> None:
        self.should_have_visible_ui_element(reset_password_required_message)

    def should_remain_on_reset_password_page(self) -> None:
        with self.step("Verify page remains on reset password form"):
            self.wait_for_path(self.path)

    def should_redirect_to_login_page(self) -> None:
        with self.step("Verify redirect to login page"):
            self.wait_for_path(LOGIN_PATH)
