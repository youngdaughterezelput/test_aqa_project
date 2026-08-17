from playwright.sync_api import expect

from components.dashboard_widget_component import PieChartWidgetComponent
from components.header_component import HeaderComponent
from components.sidebar_component import SidebarComponent
from config.settings import settings
from helpers.locators import get_dashboard_header
from helpers.paths import DASHBOARD_PATH
from pages.base_page import BasePage


class DashboardPage(BasePage):
    path = DASHBOARD_PATH

    def __init__(self, helper):
        super().__init__(helper)
        self.dashboard_header = get_dashboard_header(helper)
        self.header = HeaderComponent(helper)
        self.sidebar = SidebarComponent(helper)
        self.employee_distribution_by_sub_unit_widget = PieChartWidgetComponent(
            helper,
            "Employee Distribution by Sub Unit",)
        self.employee_distribution_by_location_widget = PieChartWidgetComponent(
            helper,
            "Employee Distribution by Location",)

    def should_be_opened(self) -> None:
        with self.step("Verify dashboard page is opened"):
            self.wait_for_path(self.path)
            expect(self.dashboard_header).to_be_visible(timeout=settings.timeout)
            expect(self.header.container).to_be_visible(timeout=settings.timeout)
            expect(self.header.user_menu_trigger).to_be_visible(timeout=settings.timeout)

    def should_have_available_upgrade_button(self) -> None:
        with self.step("Verify Upgrade button is available"):
            expect(self.header.upgrade_button).to_be_visible(timeout=settings.timeout)
            expect(self.header.upgrade_button).to_be_enabled(timeout=settings.timeout)

    def open_user_menu(self) -> None:
        with self.step("Open header user menu"):
            self.header.open_user_menu()

    def should_have_open_user_menu(self) -> None:
        with self.step("Verify header user menu is open"):
            expect(self.header.user_menu).to_be_visible(timeout=settings.timeout)

    def should_have_sidebar_menu_items(self) -> None:
        with self.step("Verify sidebar menu items are available"):
            expect(self.sidebar.menu).to_be_visible(timeout=settings.timeout)
            expect(self.sidebar.menu_items.first).to_be_visible(timeout=settings.timeout)
            assert self.sidebar.menu_items.count() > 0, (
                "Sidebar menu does not contain any menu items.")

    def search_sidebar_menu(self, query: str) -> None:
        with self.step(f"Search sidebar menu for '{query}'"):
            expect(self.sidebar.search_input).to_be_visible(timeout=settings.timeout)
            self.sidebar.search(query)

    def should_have_sidebar_search_results(self, query: str) -> None:
        with self.step(f"Verify sidebar search results for '{query}'"):
            expect(self.sidebar.menu_items.first).to_be_visible(timeout=settings.timeout)
            visible_item_names = self.sidebar.visible_menu_item_names()
            assert visible_item_names, (
                f"Sidebar search for '{query}' returned no visible menu items.")
            assert all(query.casefold() in name.casefold() for name in visible_item_names), (
                f"Sidebar search for '{query}' returned unexpected items: "
                f"{visible_item_names}.")

    def open_sidebar_menu_item(self, name: str, expected_path: str) -> None:
        with self.step(f"Click sidebar menu item '{name}'"):
            menu_item = self.sidebar.menu_item(name)
            expect(menu_item).to_be_visible(timeout=settings.timeout)
            self.sidebar.click_menu_item(name)
            self.wait_for_path(expected_path)

    def collapse_sidebar(self) -> None:
        with self.step("Collapse dashboard sidebar"):
            self.helper.sidebar.collapse()

    def scroll_to_widget(self, widget: PieChartWidgetComponent) -> None:
        with self.step(f"Scroll to widget '{widget.title}'"):
            self.scroll_to(widget.chart_canvas)

    def should_show_widget_pie_chart(self, widget: PieChartWidgetComponent) -> None:
        with self.step(f"Verify widget '{widget.title}' pie chart and icon are visible"):
            self.scroll_to_widget(widget)
            expect(widget.icon).to_be_visible(timeout=settings.timeout)
            expect(widget.chart_canvas).to_be_visible(timeout=settings.timeout)

    def hover_over_widget_segment(self, widget: PieChartWidgetComponent) -> None:
        with self.step(f"Hover over widget '{widget.title}' pie chart segment"):
            self.scroll_to_widget(widget)
            self.helper.element.hover_until_visible(
                widget.chart_canvas,
                widget.chart_tooltip,
                self.helper.element.build_radial_hover_positions(widget.chart_canvas),)

    def should_show_widget_tooltip(self, widget: PieChartWidgetComponent) -> None:
        with self.step(f"Verify widget '{widget.title}' pie chart tooltip is visible"):
            expect(widget.chart_tooltip).to_be_visible(timeout=settings.timeout)

    def click_first_widget_legend_item(self, widget: PieChartWidgetComponent) -> None:
        with self.step(f"Click first legend item in widget '{widget.title}'"):
            self.scroll_to_widget(widget)
            self.helper.element.click(widget.first_legend_item)

    def should_strike_through_first_widget_legend_item(
        self,
        widget: PieChartWidgetComponent,) -> None:
        with self.step(f"Verify first legend item in widget '{widget.title}' is struck through"):
            self.scroll_to_widget(widget)
            expect(widget.first_legend_label).to_have_css(
                "text-decoration-line",
                "line-through",
                timeout=settings.timeout,)

    def get_widget_chart_snapshot(self, widget: PieChartWidgetComponent) -> str:
        self.scroll_to_widget(widget)
        return widget.chart_canvas.evaluate("canvas => canvas.toDataURL()")

    def wait_until_widget_chart_changes(
        self,
        widget: PieChartWidgetComponent,
        previous_snapshot: str,) -> str:
        with self.step(f"Wait until widget '{widget.title}' pie chart changes"):
            self.scroll_to_widget(widget)
            return self.helper.element.wait_until_canvas_changes(
                widget.chart_canvas,
                previous_snapshot,)
