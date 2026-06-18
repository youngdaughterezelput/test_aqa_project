from helpers.locators import (
    get_dashboard_widget_chart_canvas,
    get_dashboard_widget_chart_tooltip,
    get_dashboard_widget_first_legend_item,
    get_dashboard_widget_first_legend_label,
    get_dashboard_widget_icon,
    get_dashboard_widget_legend,
    get_dashboard_widget_root,
)


class PieChartWidgetComponent:
    def __init__(self, helper, title: str):
        self.title = title
        self.root = get_dashboard_widget_root(helper, title)
        self.icon = get_dashboard_widget_icon(helper, title)
        self.chart_canvas = get_dashboard_widget_chart_canvas(helper, title)
        self.chart_tooltip = get_dashboard_widget_chart_tooltip(helper)
        self.legend = get_dashboard_widget_legend(helper, title)
        self.first_legend_item = get_dashboard_widget_first_legend_item(helper, title)
        self.first_legend_label = get_dashboard_widget_first_legend_label(helper, title)
