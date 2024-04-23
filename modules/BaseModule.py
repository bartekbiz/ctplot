from plots.AnimatedPlot import AnimatedPlot

from controls.base.Frame import Frame
from controls.OpenCSVButton import OpenCSVButton
from controls.CloseButton import CloseButton
from controls.base.Separator import Separator
from controls.MinMaxFields import MinMaxFields
from controls.ApplyButton import ApplyButton
from controls.SpanField import SpanField
from controls.DeviceRangeField import DeviceRangeField

from tkinter import DoubleVar


class BaseModule:
    def __init__(self, app, plot_1_y_title="", plot_2_y_title="", plot_3_y_title=""):
        self.app = app

        # Plot related
        self.data = {"x": [], "y": []}
        self.plot_frame = Frame(self.app.column_2_frame, row=0, col=2, rowspan=10)
        self.plot = AnimatedPlot(self.plot_frame, self.app, self.data, row=0, col=4)
        self.plot.create_empty_plot()

        self.plot_1_y_title = plot_1_y_title
        self.plot_2_y_title = plot_2_y_title
        self.plot_3_y_title = plot_3_y_title

        # Controls
        self.buttons_frame = Frame(self.app.column_0_frame, row=1, col=0)
        self.open_csv_button = OpenCSVButton(self.buttons_frame, self, row=0, col=0)
        self.close_button = CloseButton(self.buttons_frame, self, row=1, col=0)
        self.under_buttons_sep = Separator(self.buttons_frame, row=3, col=0)

        self.user_inputs_frame = Frame(self.app.column_0_frame, row=2, col=0)
        self.span_field = SpanField(self.user_inputs_frame, self, row=0)
        self.at_the_bottom_sep = Separator(self.user_inputs_frame, row=1, col=0)

        self.plot_manipulation_frame = Frame(self.app.column_1_frame, row=0, col=0, rowspan=4)
        self.minmax_fields = MinMaxFields(self.plot_manipulation_frame, self, start_row=4, start_col=2)
        self.apply_button = ApplyButton(self.plot_manipulation_frame, self, row=20, col=3)

        # Device range
        self.device_range_min = DoubleVar()
        self.device_range_max = DoubleVar()
        # self.device_range_field = DeviceRangeField(self)

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
