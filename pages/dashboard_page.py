from playwright.sync_api import expect

from components.dashboard_widget_component import EmployeeDistributionWidgetComponent
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
        self.employee_distribution_widget = EmployeeDistributionWidgetComponent(helper)

    def should_be_opened(self) -> None:
        with self.step("Verify dashboard page is opened"):
            self.wait_for_path(self.path)
            expect(self.dashboard_header).to_be_visible(timeout=settings.timeout)
            expect(self.user_dropdown).to_be_visible(timeout=settings.timeout)

    def collapse_sidebar(self) -> None:
        with self.step("Collapse dashboard sidebar"):
            self.helper.sidebar.collapse()

    def scroll_to_employee_distribution_widget(self) -> None:
        with self.step("Scroll to employee distribution widget"):
            self.scroll_to(self.employee_distribution_widget.chart_canvas)

    def should_show_employee_distribution_pie_chart(self) -> None:
        with self.step("Verify employee distribution pie chart is visible"):
            self.scroll_to_employee_distribution_widget()
            expect(self.employee_distribution_widget.chart_canvas).to_be_visible(
                timeout=settings.timeout)

    def hover_over_employee_distribution_segment(self) -> None:
        with self.step("Hover over employee distribution pie chart segment"):
            self.scroll_to_employee_distribution_widget()
            self.helper.element.hover_until_visible(
                self.employee_distribution_widget.chart_canvas,
                self.employee_distribution_widget.chart_tooltip,
                self._employee_distribution_hover_positions(),)

    def should_show_employee_distribution_tooltip(self) -> None:
        with self.step("Verify employee distribution pie chart tooltip is visible"):
            expect(self.employee_distribution_widget.chart_tooltip).to_be_visible(
                timeout=settings.timeout)

    def click_first_employee_distribution_legend_item(self) -> None:
        with self.step("Click first employee distribution legend item"):
            self.scroll_to_employee_distribution_widget()
            self.helper.element.click(self.employee_distribution_widget.first_legend_item)

    def should_strike_through_first_employee_distribution_legend_item(self) -> None:
        with self.step("Verify first employee distribution legend item is struck through"):
            expect(
                self.employee_distribution_widget.first_legend_label
            ).to_have_css("text-decoration-line", "line-through", timeout=settings.timeout)

    def get_employee_distribution_chart_snapshot(self) -> str:
        self.scroll_to_employee_distribution_widget()
        return self.employee_distribution_widget.chart_canvas.evaluate(
            "canvas => canvas.toDataURL()")

    def wait_until_employee_distribution_chart_changes(self, previous_snapshot: str) -> str:
        with self.step("Wait until employee distribution pie chart changes"):
            self.scroll_to_employee_distribution_widget()
            return self.helper.element.wait_until_canvas_changes(
                self.employee_distribution_widget.chart_canvas,
                previous_snapshot,)

    def _employee_distribution_hover_positions(self) -> list[dict[str, float]]:
        box = self.employee_distribution_widget.chart_canvas.bounding_box()
        if box is None:
            raise AssertionError("Employee distribution chart canvas bounding box is unavailable.")
        width = box["width"]
        height = box["height"]
        center_x = width / 2
        center_y = height / 2
        radius = min(width, height) * 0.32
        return [
            {"x": center_x + radius, "y": center_y},
            {"x": center_x + radius * 0.8, "y": center_y - radius * 0.6},
            {"x": center_x + radius * 0.2, "y": center_y - radius},
            {"x": center_x - radius * 0.5, "y": center_y - radius * 0.85},
            {"x": center_x - radius, "y": center_y},
            {"x": center_x - radius * 0.7, "y": center_y + radius * 0.7},
            {"x": center_x + radius * 0.1, "y": center_y + radius},
            {"x": center_x + radius * 0.9, "y": center_y + radius * 0.35},]
