import allure
import pytest
from playwright.sync_api import Browser, BrowserType, Page, Playwright, sync_playwright

from config.settings import settings
from config.test_data import admin_user as default_admin_user
from helpers.ui_helper import UiHelper
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.reset_password_page import ResetPasswordPage


def _get_browser_type(playwright: Playwright) -> BrowserType:
    browser_name = settings.browser.lower()
    browser_map = {
        "chromium": playwright.chromium,
        "firefox": playwright.firefox,
        "webkit": playwright.webkit,
    }
    if browser_name not in browser_map:
        raise ValueError(
            f"Unsupported browser '{settings.browser}'. Use one of: chromium, firefox, webkit."
        )
    return browser_map[browser_name]


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as playwright:
        yield playwright


@pytest.fixture(scope="session")
def browser(playwright_instance: Playwright) -> Browser:
    browser_type = _get_browser_type(playwright_instance)
    browser = browser_type.launch(headless=settings.headless)
    yield browser
    browser.close()


@pytest.fixture
def page(browser: Browser) -> Page:
    context = browser.new_context(
        viewport={
            "width": settings.viewport_width,
            "height": settings.viewport_height,
        }
    )
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture
def ui_helper(page: Page) -> UiHelper:
    helper = UiHelper(page)
    helper.set_default_timeout()
    return helper


@pytest.fixture
def login_page(ui_helper: UiHelper) -> LoginPage:
    return LoginPage(ui_helper)


@pytest.fixture
def dashboard_page(ui_helper: UiHelper) -> DashboardPage:
    return DashboardPage(ui_helper)


@pytest.fixture
def reset_password_page(ui_helper: UiHelper) -> ResetPasswordPage:
    return ResetPasswordPage(ui_helper)


@pytest.fixture
def admin_user():
    return default_admin_user


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)


@pytest.fixture(autouse=True)
def attach_screenshot_on_failure(request, page: Page):
    yield
    for phase in ("setup", "call"):
        report = getattr(request.node, f"rep_{phase}", None)
        if report and report.failed:
            allure.attach(
                page.screenshot(full_page=True),
                name=f"{request.node.name} - {phase} failed",
                attachment_type=allure.attachment_type.PNG,
            )
            break
