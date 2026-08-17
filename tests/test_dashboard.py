import pytest

from helpers.paths import ADMIN_USERS_PATH


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
@pytest.mark.smoke
def test_dashboard_upgrade_button_is_available(login_page, dashboard_page, admin_user):
    open_dashboard(login_page, dashboard_page, admin_user)
    dashboard_page.should_have_available_upgrade_button()


@pytest.mark.smoke_dashboard
def test_dashboard_user_menu_can_be_opened(login_page, dashboard_page, admin_user):
    open_dashboard(login_page, dashboard_page, admin_user)
    dashboard_page.open_user_menu()
    dashboard_page.should_have_open_user_menu()


@pytest.mark.smoke_dashboard
def test_dashboard_sidebar_contains_menu_items(login_page, dashboard_page, admin_user):
    open_dashboard(login_page, dashboard_page, admin_user)
    dashboard_page.should_have_sidebar_menu_items()


@pytest.mark.smoke_dashboard
def test_dashboard_sidebar_menu_item_opens_page(login_page, dashboard_page, admin_user):
    open_dashboard(login_page, dashboard_page, admin_user)
    dashboard_page.open_sidebar_menu_item("Admin", ADMIN_USERS_PATH)


@pytest.mark.smoke_dashboard
def test_dashboard_sidebar_search_filters_menu_items(login_page, dashboard_page, admin_user):
    open_dashboard(login_page, dashboard_page, admin_user)
    dashboard_page.search_sidebar_menu("Admin")
    dashboard_page.should_have_sidebar_search_results("Admin")


@pytest.mark.smoke_dashboard
def test_employee_distribution_pie_chart_is_visible_after_scroll(
    login_page,
    dashboard_page,
    admin_user,):
    open_dashboard(login_page, dashboard_page, admin_user)
    widget = dashboard_page.employee_distribution_by_sub_unit_widget
    dashboard_page.scroll_to_widget(widget)
    dashboard_page.should_show_widget_pie_chart(widget)


@pytest.mark.smoke_dashboard
def test_employee_distribution_tooltip_is_shown_on_segment_hover(
    login_page,
    dashboard_page,
    admin_user,):
    open_dashboard(login_page, dashboard_page, admin_user)
    widget = dashboard_page.employee_distribution_by_sub_unit_widget
    dashboard_page.hover_over_widget_segment(widget)
    dashboard_page.should_show_widget_tooltip(widget)


@pytest.mark.smoke_dashboard
def test_employee_distribution_legend_item_is_struck_through_after_click(
    login_page,
    dashboard_page,
    admin_user,):
    open_dashboard(login_page, dashboard_page, admin_user)
    widget = dashboard_page.employee_distribution_by_sub_unit_widget
    dashboard_page.click_first_widget_legend_item(widget)
    dashboard_page.should_strike_through_first_widget_legend_item(widget)


@pytest.mark.smoke_dashboard
def test_employee_distribution_pie_chart_changes_after_legend_click(
    login_page,
    dashboard_page,
    admin_user,):
    open_dashboard(login_page, dashboard_page, admin_user)
    widget = dashboard_page.employee_distribution_by_sub_unit_widget
    initial_chart_snapshot = dashboard_page.get_widget_chart_snapshot(widget)
    dashboard_page.click_first_widget_legend_item(widget)
    updated_chart_snapshot = dashboard_page.wait_until_widget_chart_changes(
        widget,
        initial_chart_snapshot,)
    assert initial_chart_snapshot != updated_chart_snapshot, (
        "Employee distribution pie chart did not change after clicking the first legend item.")


@pytest.mark.smoke_dashboard
def test_employee_distribution_by_location_pie_chart_is_visible_after_scroll(
    login_page,
    dashboard_page,
    admin_user,):
    open_dashboard(login_page, dashboard_page, admin_user)
    widget = dashboard_page.employee_distribution_by_location_widget
    dashboard_page.scroll_to_widget(widget)
    dashboard_page.should_show_widget_pie_chart(widget)


@pytest.mark.smoke_dashboard
def test_employee_distribution_by_location_tooltip_is_shown_on_segment_hover(
    login_page,
    dashboard_page,
    admin_user,):
    open_dashboard(login_page, dashboard_page, admin_user)
    widget = dashboard_page.employee_distribution_by_location_widget
    dashboard_page.hover_over_widget_segment(widget)
    dashboard_page.should_show_widget_tooltip(widget)


@pytest.mark.smoke_dashboard
def test_employee_distribution_by_location_legend_item_is_struck_through_after_click(
    login_page,
    dashboard_page,
    admin_user,):
    open_dashboard(login_page, dashboard_page, admin_user)
    widget = dashboard_page.employee_distribution_by_location_widget
    dashboard_page.click_first_widget_legend_item(widget)
    dashboard_page.should_strike_through_first_widget_legend_item(widget)


@pytest.mark.smoke_dashboard
def test_employee_distribution_by_location_pie_chart_changes_after_legend_click(
    login_page,
    dashboard_page,
    admin_user,):
    open_dashboard(login_page, dashboard_page, admin_user)
    widget = dashboard_page.employee_distribution_by_location_widget
    initial_chart_snapshot = dashboard_page.get_widget_chart_snapshot(widget)
    dashboard_page.click_first_widget_legend_item(widget)
    updated_chart_snapshot = dashboard_page.wait_until_widget_chart_changes(
        widget,
        initial_chart_snapshot,)
    assert initial_chart_snapshot != updated_chart_snapshot, (
        "Employee distribution by location pie chart did not change after clicking the first "
        "legend item.")
