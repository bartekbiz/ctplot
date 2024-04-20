import controls.SpanField
import controls.ApplyButton

from plots.AnimatedPlot import AnimatedPlot
from controls.MinMaxFields import XMinMaxFields
from controls.MinMaxFields import YMinMaxFields


class BaseModule:
    def __init__(self, app):
        self.app = app

        # Plot related
        self.data = {"x": [], "y": []}
        self.plot = AnimatedPlot(app, self.data)

        # MinMax fields
        self.x_minmax_fields = XMinMaxFields(self)
        self.y_minmax_fields = YMinMaxFields(self)

        # Apply button
        self.apply_button = None
        self.create_apply_button()

        self.create_custom_span()

    def create_apply_button(self):
        controls.ApplyButton.create_apply_button(self)

    def apply(self, *event):
        self.plot.create_plot()

    def create_custom_span(self):
        controls.SpanField.create_custom_span(self)

    def get_name(self):
        raise NotImplementedError()

    def close(self, *event):
        self.plot.close_plot()
