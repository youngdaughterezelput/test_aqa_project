import pytest


@pytest.mark.smoke
def test_dashboard_is_available_for_authorized_user(login_page, dashboard_page, admin_user):
    login_page.open()
    login_page.login(admin_user)
    dashboard_page.should_be_opened()
