from plots.AnimatedPlot import AnimatedPlot
from controls.MinMaxFields import XMinMaxFields
from controls.MinMaxFields import YMinMaxFields
from controls.ApplyButton import ApplyButton
from controls.SpanField import SpanField
from controls.DeviceRangeField import DeviceRangeField

from tkinter import DoubleVar


class BaseModule:
    def __init__(self, app):
        self.app = app

        # Plot related
        self.data = {"x": [], "y": []}
        self.plot = AnimatedPlot(self.app, self.data)
        self.plot.create_empty_plot()

        # Controls
        self.apply_button = ApplyButton(self)
        self.span_field = SpanField(self)

        # Device range
        self.device_range_min = DoubleVar()
        self.device_range_max = DoubleVar()
        # self.device_range_field = DeviceRangeField(self)

    def apply(self, *event):
        self.plot.update_plot_params()

    def get_name(self):
        raise NotImplementedError()

    def close_module(self, *event):
        self.plot.close_plot()

        # self.x_minmax_fields.destroy()
        # self.y_minmax_fields.destroy()
        self.apply_button.destroy()
        self.span_field.destroy()
