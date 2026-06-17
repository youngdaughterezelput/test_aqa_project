from playwright.sync_api import expect

from config.settings import settings
from helpers.locators import get_by_class, get_by_role
from helpers.paths import DASHBOARD_PATH
from pages.base_page import BasePage


class DashboardPage(BasePage):
    path = DASHBOARD_PATH

    def __init__(self, helper):
        super().__init__(helper)
        self.dashboard_header = get_by_role(helper, "heading", "Dashboard")
        self.user_dropdown = get_by_class(helper, "oxd-userdropdown")

    def should_be_opened(self) -> None:
        with self.step("Verify dashboard page is opened"):
            self.wait_for_url(self.path)
            expect(self.dashboard_header).to_be_visible(timeout=settings.timeout)
            expect(self.user_dropdown).to_be_visible(timeout=settings.timeout)
