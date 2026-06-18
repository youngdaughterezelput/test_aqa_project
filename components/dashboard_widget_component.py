from helpers.locators import (
    get_employee_distribution_chart_canvas,
    get_employee_distribution_chart_tooltip,
    get_employee_distribution_first_legend_item,
    get_employee_distribution_first_legend_label,
    get_employee_distribution_legend,
    get_employee_distribution_widget,
)


class EmployeeDistributionWidgetComponent:
    def __init__(self, helper):
        self.root = get_employee_distribution_widget(helper)
        self.chart_canvas = get_employee_distribution_chart_canvas(helper)
        self.chart_tooltip = get_employee_distribution_chart_tooltip(helper)
        self.legend = get_employee_distribution_legend(helper)
        self.first_legend_item = get_employee_distribution_first_legend_item(helper)
        self.first_legend_label = get_employee_distribution_first_legend_label(helper)
