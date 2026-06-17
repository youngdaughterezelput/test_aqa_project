from playwright.sync_api import expect

from config.settings import settings
from helpers.locators import get_by_class, get_by_placeholder, get_by_role
from helpers.paths import REQUEST_PASSWORD_RESET_PATH
from pages.base_page import BasePage


class ResetPasswordPage(BasePage):
    path = REQUEST_PASSWORD_RESET_PATH

    def __init__(self, helper):
        super().__init__(helper)
        self.card_container = get_by_class(helper, "orangehrm-card-container")
        self.username_input = get_by_placeholder(helper, "Username")
        self.reset_password_button = get_by_role(helper, "button", "Reset Password")

    def should_be_opened(self) -> None:
        with self.step("Verify reset password page URL"):
            self.wait_for_url(self.path)

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
                    for index in range(self.card_container.count())
                ]
                assert any(
                    visible_cards
                ), "Reset password card container is present but not visible."
                return
            raise AssertionError("Reset password card container was not found on the page.")
