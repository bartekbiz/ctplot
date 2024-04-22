from plots.AnimatedPlot import AnimatedPlot

from controls.OpenCSVButton import OpenCSVButton
from controls.CloseButton import CloseButton
from controls.Separators import UnderButtonsSeparator
from controls.MinMaxFields import XMinMaxFields
from controls.MinMaxFields import YMinMaxFields
from controls.ApplyButton import ApplyButton
from controls.SpanField import SpanField
from controls.Separators import UnderEverythingSeparator
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
        self.open_csv_button = OpenCSVButton(self)
        self.close_button = CloseButton(self)
        self.under_buttons_sep = UnderButtonsSeparator(self)
        self.x_minmax_fields = XMinMaxFields(self)
        self.y_minmax_fields = YMinMaxFields(self)
        self.span_field = SpanField(self,16)
        self.apply_button = ApplyButton(self, 17)
        self.under_everything_sep = UnderEverythingSeparator(self)

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


        self.open_csv_button.destroy()
        self.close_button.destroy()
        self.under_buttons_sep.destroy()
#         self.x_minmax_fields.destroy()
#         self.y_minmax_fields.destroy()
        self.apply_button.destroy()
        self.span_field.destroy()
        self.under_everything_sep.destroy()
