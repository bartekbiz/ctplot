from plots.AnimatedPlot import AnimatedPlot

from controls.base.Frame import Frame

from controls.ButtonsFrame.ButtonsFrame import ButtonsFrame
from controls.InputsFrame.InputsFrame import InputsFrame
from controls.PlotManipulationFrame.PlotManipulationFrame import PlotManipulationFrame

from tkinter import DoubleVar


class BaseModule:
    def __init__(self, app, plot_values: dict, plot_x_name="t"):
        self.app = app

        # Plot related
        self.data = {"x": [], "y": []}
        self.plot_names = list(plot_values.keys())
        self.plot_units = list(plot_values.values())
        self.plots_x_name = plot_x_name
        self.plot_frame = Frame(self.app.column_2_frame, row=0)
        self.plot = AnimatedPlot(
            self.plot_frame,
            self.app,
            self.data,
            self.plot_names,
            self.plot_units,
            self.plots_x_name
        )
        self.plot.create_empty_plot()

        # Create frames
        self.buttons_frame = ButtonsFrame(self.app, self)

        self.device_range_min = DoubleVar()
        self.device_range_max = DoubleVar()
        self.inputs_frame = InputsFrame(self.app, self)

        self.plot_manipulation_frame = PlotManipulationFrame(self.app, self)

        # TODO: Bind updating statistics to auto event
        self.app.bind("r", self.update_plot_stats)

    def apply(self, *event):
        self.plot.update_plot_params()

    def get_name(self):
        raise NotImplementedError()

    def destroy(self, *event):
        self.plot.close_plot()

        # Destroy controls
        self.plot_frame.destroy()
        self.buttons_frame.destroy()
        self.inputs_frame.destroy()
        self.plot_manipulation_frame.destroy()

    def update_plot_stats(self, *event):
        self.inputs_frame.plot_statistics.max_value.update_value(self.plot.get_max_value())
        self.inputs_frame.plot_statistics.min_value.update_value(self.plot.get_min_value())
        self.inputs_frame.plot_statistics.max_velocity.update_value(self.plot.get_max_velocity())
        self.inputs_frame.plot_statistics.min_velocity.update_value(self.plot.get_min_velocity())
        self.inputs_frame.plot_statistics.max_acceleration.update_value(self.plot.get_max_acceleration())
        self.inputs_frame.plot_statistics.min_acceleration.update_value(self.plot.get_min_acceleration())

    def reset_ranges(self):
        self.minmax_fields.x_minmax_fields_1.x_min_entry.set(0)
        # self.minmax_fields.x_minmax_fields_1.x_max_entry.set(0)
        # self.minmax_fields.y_minmax_fields_1.y_min_entry.set(0)
        # self.minmax_fields.y_minmax_fields_1.y_max_entry.set(0)
        #
        # self.minmax_fields.x_minmax_fields_2.x_min_entry.set(0)
        # self.minmax_fields.x_minmax_fields_2.x_max_entry.set(0)
        # self.minmax_fields.y_minmax_fields_2.y_min_entry.set(0)
        # self.minmax_fields.y_minmax_fields_2.y_max_entry.set(0)
        #
        # self.minmax_fields.x_minmax_fields_3.x_min_entry.set(0)
        # self.minmax_fields.x_minmax_fields_3.x_max_entry.set(0)
        # self.minmax_fields.y_minmax_fields_3.y_min_entry.set(0)
        # self.minmax_fields.y_minmax_fields_3.y_max_entry.set(0)
