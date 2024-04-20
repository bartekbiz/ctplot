import controls.SpanField
import controls.ApplyButton

from plots.AnimatedPlot import AnimatedPlot
from controls.MinMaxFields import XMinMaxFields
from controls.MinMaxFields import YMinMaxFields
from controls.ApplyButton import ApplyButton
from controls.SpanField import SpanField


class BaseModule:
    def __init__(self, app):
        self.app = app

        # Plot related
        self.data = {"x": [], "y": []}
        self.plot = AnimatedPlot(self.app, self.data)
        self.plot.create_empty_plot()

        # Controls
        self.x_minmax_fields = XMinMaxFields(self)
        self.y_minmax_fields = YMinMaxFields(self)
        self.apply_button = ApplyButton(self)
        self.span_field = SpanField(self)

    def get_name(self):
        raise NotImplementedError()

    def apply(self, *event):
        self.plot.update_plot_params()

    def close_module(self, *event):
        self.plot.close_plot()
