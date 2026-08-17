import pytest

from config.test_data import (
    LoginUser,
    login_branding_container,
    login_branding_logo,
    login_social_icons,
    reset_password_request_user,
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

"""
504 error on server
"""
"""@pytest.mark.smoke_reset
def test_reset_password_redirects_to_confirmation_page(login_page, reset_password_page):
    login_page.open()
    login_page.click_forgot_password()
    reset_password_page.submit_reset_password_request(reset_password_request_user)
    reset_password_page.should_redirect_to_confirmation_page()"""


@pytest.mark.smoke_reset
def test_reset_password_with_empty_username_shows_required_error(
    login_page,
    reset_password_page,):
    login_page.open()
    login_page.click_forgot_password()
    reset_password_page.click_reset_password()
    reset_password_page.should_remain_on_reset_password_page()
    reset_password_page.should_show_required_error_for_username()


@pytest.mark.smoke_reset
def test_reset_password_cancel_redirects_to_login_page(login_page, reset_password_page):
    login_page.open()
    login_page.click_forgot_password()
    reset_password_page.click_cancel()
    reset_password_page.should_redirect_to_login_page()


@pytest.mark.smoke
def test_login_page_displays_all_social_icons(login_page):
    login_page.open()
    login_page.should_have_ui_element_collection(login_social_icons)


@pytest.mark.smoke
def test_login_page_displays_branding(login_page):
    login_page.open()
    login_page.should_have_visible_ui_element(login_branding_container)
    login_page.should_have_present_ui_element(login_branding_logo)


@pytest.mark.smoke
def test_login_page_copyright_contains_link(login_page):
    login_page.open()
    login_page.should_have_copyright_link()


@pytest.mark.smoke
def test_login_page_form_container_has_content(login_page):
    login_page.open()
    login_page.should_have_login_form_content()
