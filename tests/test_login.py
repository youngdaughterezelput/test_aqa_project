import pytest

from config.test_data import (
    LoginUser,
    login_branding_container,
    login_branding_logo,
    login_social_icons,
)


@pytest.mark.smoke
def test_successful_login(login_page, dashboard_page, admin_user):
    login_page.open()
    login_page.login(admin_user)
    dashboard_page.should_be_opened()


@pytest.mark.smoke
def test_login_with_invalid_password(login_page):
    login_page.open()
    invalid_user = LoginUser(username="Admin", password="wrong_password")
    login_page.login(invalid_user)
    login_page.should_have_invalid_credentials_error()


@pytest.mark.smoke
def test_forgot_password_redirects_to_reset_page(login_page, reset_password_page):
    login_page.open()
    login_page.click_forgot_password()
    reset_password_page.should_be_opened()


@pytest.mark.smoke
def test_reset_password_page_displays_expected_elements(login_page, reset_password_page):
    login_page.open()
    login_page.click_forgot_password()
    reset_password_page.should_display_reset_password_form()
    reset_password_page.should_display_card_container()


@pytest.mark.smoke
def test_login_page_displays_all_social_icons(login_page):
    login_page.open()
    login_page.should_have_ui_element_collection(login_social_icons)


@pytest.mark.smoke
def test_login_page_displays_branding(login_page):
    login_page.open()
    login_page.should_have_visible_ui_element(login_branding_container)
    login_page.should_have_present_ui_element(login_branding_logo)
