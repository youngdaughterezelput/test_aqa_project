import pytest


def open_dashboard(login_page, dashboard_page, admin_user) -> None:
    login_page.open()
    login_page.login(admin_user)
    dashboard_page.should_be_opened()


@pytest.mark.smoke_dashboard
@pytest.mark.smoke
def test_dashboard_is_available_for_authorized_user(login_page, dashboard_page, admin_user):
    open_dashboard(login_page, dashboard_page, admin_user)
    dashboard_page.collapse_sidebar()


@pytest.mark.smoke_dashboard
def test_employee_distribution_pie_chart_is_visible_after_scroll(
    login_page,
    dashboard_page,
    admin_user,):
    open_dashboard(login_page, dashboard_page, admin_user)
    dashboard_page.scroll_to_employee_distribution_widget()
    dashboard_page.should_show_employee_distribution_pie_chart()


@pytest.mark.smoke_dashboard
def test_employee_distribution_tooltip_is_shown_on_segment_hover(
    login_page,
    dashboard_page,
    admin_user,):
    open_dashboard(login_page, dashboard_page, admin_user)
    dashboard_page.hover_over_employee_distribution_segment()
    dashboard_page.should_show_employee_distribution_tooltip()


@pytest.mark.smoke_dashboard
def test_employee_distribution_legend_item_is_struck_through_after_click(
    login_page,
    dashboard_page,
    admin_user,):
    open_dashboard(login_page, dashboard_page, admin_user)
    dashboard_page.click_first_employee_distribution_legend_item()
    dashboard_page.should_strike_through_first_employee_distribution_legend_item()


@pytest.mark.smoke_dashboard
def test_employee_distribution_pie_chart_changes_after_legend_click(
    login_page,
    dashboard_page,
    admin_user,):
    open_dashboard(login_page, dashboard_page, admin_user)
    initial_chart_snapshot = dashboard_page.get_employee_distribution_chart_snapshot()
    dashboard_page.click_first_employee_distribution_legend_item()
    updated_chart_snapshot = dashboard_page.wait_until_employee_distribution_chart_changes(
        initial_chart_snapshot)
    assert initial_chart_snapshot != updated_chart_snapshot, (
        "Employee distribution pie chart did not change after clicking the first legend item.")
