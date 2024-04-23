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
    def __init__(self, app, plot_names: list, plot_x_name="t"):
        self.app = app

        # Create frames
        self.plot_frame = Frame(self.app.column_2_frame, row=0)
        self.buttons_frame = Frame(self.app.column_0_frame, row=1)
        self.user_inputs_frame = Frame(self.app.column_0_frame, row=2)
        self.plot_manipulation_frame = Frame(self.app.column_1_frame, row=0)

        # Plot related
        self.data = {"x": [], "y": []}
        self.plot_names = plot_names
        self.plots_x_name = plot_x_name

        self.plot = AnimatedPlot(
            self.plot_frame,
            self.app,
            self.data,
            plot_names,
            self.plots_x_name
        )
        self.plot.create_empty_plot()

        # Controls
        self.open_csv_button = OpenCSVButton(self.buttons_frame, self, row=0)
        self.close_button = CloseButton(self.buttons_frame, self, row=1)
        Separator(self.buttons_frame, row=3)

        Separator(self.user_inputs_frame, row=1)
        self.minmax_fields = MinMaxFields(self.plot_manipulation_frame, self, start_row=0)
        self.span_field = SpanField(self.plot_manipulation_frame, self, row=16)
        Separator(self.plot_manipulation_frame, row=17)
        self.apply_button = ApplyButton(self.plot_manipulation_frame, self, row=18, col=1)

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
        self.plot_frame.destroy()
        self.buttons_frame.destroy()
        self.user_inputs_frame.destroy()
        self.plot_manipulation_frame.destroy()
