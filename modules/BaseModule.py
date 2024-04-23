from plots.AnimatedPlot import AnimatedPlot

from controls.OpenCSVButton import OpenCSVButton
from controls.CloseButton import CloseButton
from controls.base.Separator import Separator
from controls.MinMaxFields import MinMaxFields
from controls.ApplyButton import ApplyButton
from controls.SpanField import SpanField
from controls.DeviceRangeField import DeviceRangeField
from controls.PlotValues.PlotStatistics import PlotStatistics

from tkinter import DoubleVar


class BaseModule:
    def __init__(self, app, plot_1_y_title="", plot_2_y_title="", plot_3_y_title=""):
        self.app = app

        # Plot related
        self.data = {"x": [], "y": []}
        self.plot = AnimatedPlot(self.app, self.data)
        self.plot.create_empty_plot()

        self.plot_1_y_title = plot_1_y_title
        self.plot_2_y_title = plot_2_y_title
        self.plot_3_y_title = plot_3_y_title

        # Controls
        self.open_csv_button = OpenCSVButton(self, row=2)
        self.close_button = CloseButton(self, row=3)
        self.under_buttons_sep = Separator(self.app, row=4)

        self.minmax_fields = MinMaxFields(self)

        self.span_field = SpanField(self, row=98)
        self.at_the_bottom_sep = Separator(self.app, row=99)
        self.apply_button = ApplyButton(self, row=100)

        # Device range
        self.device_range_min = DoubleVar()
        self.device_range_max = DoubleVar()
        # self.device_range_field = DeviceRangeField(self)

        # Plot Statistics
        self.plot_statistics = PlotStatistics(self)
        

        #TODO: Bind updating statistics to auto event
        self.app.bind("r", self.update_plot_stats)

    def apply(self, *event):
        self.plot.update_plot_params()

    def get_name(self):
        raise NotImplementedError()

    def destroy(self, *event):
        self.plot.close_plot()

        # Destroy controls
        self.open_csv_button.destroy()
        self.close_button.destroy()
        self.under_buttons_sep.destroy()
        self.minmax_fields.destroy()
        self.apply_button.destroy()
        self.span_field.destroy()
        self.at_the_bottom_sep.destroy()

    def update_plot_stats(self, *event):
        self.plot_statistics.max_value.update_value(self.plot.get_max_value())
        self.plot_statistics.min_value.update_value(self.plot.get_min_value())
        self.plot_statistics.max_velocity.update_value(self.plot.get_max_velocity())
        self.plot_statistics.min_velocity.update_value(self.plot.get_min_velocity())
        self.plot_statistics.max_acceleration.update_value(self.plot.get_max_acceleration())
        self.plot_statistics.min_acceleration.update_value(self.plot.get_min_acceleration())
