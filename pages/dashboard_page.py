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

    def should_show_employee_distribution_pie_chart(self) -> None:
        with self.step("Verify employee distribution pie chart and icon are visible"):
            self._should_show_widget_icon_and_pie_chart(
                self.employee_distribution_by_sub_unit_widget,
                "employee distribution by sub unit",)

    def hover_over_employee_distribution_segment(self) -> None:
        with self.step("Hover over employee distribution pie chart segment"):
            self._hover_over_widget_segment(
                self.employee_distribution_by_sub_unit_widget,
                "employee distribution by sub unit",)

    def should_show_employee_distribution_tooltip(self) -> None:
        with self.step("Verify employee distribution pie chart tooltip is visible"):
            expect(self.employee_distribution_by_sub_unit_widget.chart_tooltip).to_be_visible(
                timeout=settings.timeout)

    def click_first_employee_distribution_legend_item(self) -> None:
        with self.step("Click first employee distribution legend item"):
            self._click_first_widget_legend_item(
                self.employee_distribution_by_sub_unit_widget,
                "employee distribution by sub unit",)

    def should_strike_through_first_employee_distribution_legend_item(self) -> None:
        with self.step("Verify first employee distribution legend item is struck through"):
            self._should_strike_through_first_widget_legend_item(
                self.employee_distribution_by_sub_unit_widget,
                "employee distribution by sub unit",)

    def get_employee_distribution_chart_snapshot(self) -> str:
        return self._get_widget_chart_snapshot(
            self.employee_distribution_by_sub_unit_widget,
            "employee distribution by sub unit",)

    def wait_until_employee_distribution_chart_changes(self, previous_snapshot: str) -> str:
        with self.step("Wait until employee distribution pie chart changes"):
            return self._wait_until_widget_chart_changes(
                self.employee_distribution_by_sub_unit_widget,
                previous_snapshot,
                "employee distribution by sub unit",)

    def should_show_employee_distribution_by_location_pie_chart(self) -> None:
        with self.step("Verify employee distribution by location pie chart and icon are visible"):
            self._should_show_widget_icon_and_pie_chart(
                self.employee_distribution_by_location_widget,
                "employee distribution by location",)

    def hover_over_employee_distribution_by_location_segment(self) -> None:
        with self.step("Hover over employee distribution by location pie chart segment"):
            self._hover_over_widget_segment(
                self.employee_distribution_by_location_widget,
                "employee distribution by location",)

    def should_show_employee_distribution_by_location_tooltip(self) -> None:
        with self.step("Verify employee distribution by location pie chart tooltip is visible"):
            expect(self.employee_distribution_by_location_widget.chart_tooltip).to_be_visible(
                timeout=settings.timeout)

    def click_first_employee_distribution_by_location_legend_item(self) -> None:
        with self.step("Click first employee distribution by location legend item"):
            self._click_first_widget_legend_item(
                self.employee_distribution_by_location_widget,
                "employee distribution by location",)

    def should_strike_through_first_employee_distribution_by_location_legend_item(
        self,) -> None:
        with self.step(
            "Verify first employee distribution by location legend item is struck through"):
            self._should_strike_through_first_widget_legend_item(
                self.employee_distribution_by_location_widget,
                "employee distribution by location",)

    def get_employee_distribution_by_location_chart_snapshot(self) -> str:
        return self._get_widget_chart_snapshot(
            self.employee_distribution_by_location_widget,
            "employee distribution by location",)

    def wait_until_employee_distribution_by_location_chart_changes(
        self,
        previous_snapshot: str,) -> str:
        with self.step("Wait until employee distribution by location pie chart changes"):
            return self._wait_until_widget_chart_changes(
                self.employee_distribution_by_location_widget,
                previous_snapshot,
                "employee distribution by location",)

    def _should_show_widget_icon_and_pie_chart(
        self,
        widget: PieChartWidgetComponent,
        widget_name: str,) -> None:
        self.scroll_to_widget(widget)
        expect(widget.icon).to_be_visible(timeout=settings.timeout)
        expect(widget.chart_canvas).to_be_visible(timeout=settings.timeout)

    def _hover_over_widget_segment(
        self,
        widget: PieChartWidgetComponent,
        widget_name: str,) -> None:
        self.scroll_to_widget(widget)
        self.helper.element.hover_until_visible(
            widget.chart_canvas,
            widget.chart_tooltip,
            self.helper.element.build_radial_hover_positions(widget.chart_canvas),)

    def _click_first_widget_legend_item(
        self,
        widget: PieChartWidgetComponent,
        widget_name: str,) -> None:
        self.scroll_to_widget(widget)
        self.helper.element.click(widget.first_legend_item)

    def _should_strike_through_first_widget_legend_item(
        self,
        widget: PieChartWidgetComponent,
        widget_name: str,) -> None:
        self.scroll_to_widget(widget)
        expect(widget.first_legend_label).to_have_css(
            "text-decoration-line",
            "line-through",
            timeout=settings.timeout,)

    def _get_widget_chart_snapshot(
        self,
        widget: PieChartWidgetComponent,
        widget_name: str,) -> str:
        self.scroll_to_widget(widget)
        return widget.chart_canvas.evaluate("canvas => canvas.toDataURL()")

    def _wait_until_widget_chart_changes(
        self,
        widget: PieChartWidgetComponent,
        previous_snapshot: str,
        widget_name: str,) -> str:
        self.scroll_to_widget(widget)
        return self.helper.element.wait_until_canvas_changes(
            widget.chart_canvas,
            previous_snapshot,)
