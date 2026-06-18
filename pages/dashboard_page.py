from playwright.sync_api import expect

from components.dashboard_widget_component import PieChartWidgetComponent
from config.settings import settings
from helpers.locators import get_dashboard_header, get_user_dropdown
from helpers.paths import DASHBOARD_PATH
from pages.base_page import BasePage


class DashboardPage(BasePage):
    path = DASHBOARD_PATH

    def __init__(self, helper):
        super().__init__(helper)
        self.dashboard_header = get_dashboard_header(helper)
        self.user_dropdown = get_user_dropdown(helper)
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
            expect(self.user_dropdown).to_be_visible(timeout=settings.timeout)

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
