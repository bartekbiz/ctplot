from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import tkinter as tk
from plots.MainPlot import MainPlot
from calculations.PlotCalculations import PlotCalculations


class AnimatedPlot(MainPlot):
    def __init__(self, window, app, data):
        super().__init__(window, app, data)

        self.animation = None
        self.animated_x = []
        self.animated_y = []

        self.plot_calculations = PlotCalculations()
        self.velocity_y = []
        self.acceleration_y = []

        self.counter_generator = self.counter()
        self.range_min = 0
        self.range_max = 0

        self.animation_speed = 5
        self.refresh_rate = 40

    def create_empty_plot(self):
        self.create_figure()

        self.set_plots_props()

        self.set_min_max_values()

        self.create_canvas()
        self.create_toolbar()

    def create_plot(self):
        print("\nCreating plot...")
        self.close_plot()

        self.create_empty_plot()

        self.update_ax1_data()
        self.update_ax2_ax3_data()

        self.animation = FuncAnimation(self.fig, self.update_frame, interval=10, save_count=60)

        self.app.current_module.close_button.set_is_disabled(False)

    def create_figure(self):
        self.fig, (self.ax1, self.ax2, self.ax3) = plt.subplots(3, 1, constrained_layout=True)

        self.fig.set_figwidth(6.37)
        self.fig.set_figheight(6.95)

        self.fig.supxlabel("t [s]")

    def set_plots_props(self):
        self.set_single_plot_props(self.ax1, "Wykres x(t)", "x [m]")
        self.set_single_plot_props(self.ax2, "Wykres v(t)", "v [m/s]")
        self.set_single_plot_props(self.ax3, "Wykres a(t)", "a [m/s*s]")

    @staticmethod
    def set_single_plot_props(ax: plt.axes, title, y_label):
        ax.set_title(title)
        ax.set_ylabel(y_label)
        ax.grid()

    def update_ax1_data(self):
        custom_range_min = self.range_min - 1 if self.range_min != 0 else 0

        self.ax1.plot(
            self.animated_x[custom_range_min:],
            self.animated_y[custom_range_min:],
            self.color
        )

    def update_ax2_ax3_data(self):
        v_len = len(self.velocity_y)
        v_custom_range_min = v_len - 1 if v_len != 0 else 0

        a_len = len(self.acceleration_y)
        a_custom_range_min = a_len - 1 if a_len != 0 else 0

        v_x, v_y = self.plot_calculations.calc_linear_regression(self.animated_x, self.animated_y, self.span)
        a_x, a_y = self.plot_calculations.calc_linear_regression(v_x, v_y, self.span)

        self.ax2.plot(
            v_x[v_custom_range_min:],
            v_y[v_custom_range_min:],
            self.color
        )

        self.ax3.plot(
            a_x[a_custom_range_min:],
            a_y[a_custom_range_min:],
            self.color
        )

        self.velocity_y.extend(v_y[v_len:])
        self.acceleration_y.extend(a_y[a_len:])

    def update_frame(self, frame):
        try:
            self.range_min = next(self.counter_generator)
            self.range_max = self.range_min + self.animation_speed
        except StopIteration:
            self.pause_plot()

        self.animated_x.extend(self.data["x"][self.range_min:self.range_max])
        self.animated_y.extend(self.data["y"][self.range_min:self.range_max])

        self.update_ax1_data()
        if self.range_max % self.refresh_rate == 0:
            self.update_ax2_ax3_data()

        return self.ax1, self.ax2, self.ax3

    def counter(self):
        i = 0
        while i <= len(self.data["x"]) - self.animation_speed:
            yield i
            i += self.animation_speed

    def update_plot_params(self):
        self.set_min_max_values()
        self.set_span_value()

    def pause_plot(self):
        if self.animation is None or self.animation.event_source is None:
            return

        self.animation.event_source.stop()

    def resume_plot(self):
        if self.animation is None or self.animation.event_source is None:
            return

        self.animation.event_source.start()

    def close_plot(self):
        if self.canvas is None and self.toolbar is None:
            return

        self.canvas.get_tk_widget().destroy()
        self.toolbar.destroy()
        self.canvas = None
        self.toolbar = None

        self.app.current_module.close_button.set_is_disabled(True)
        self.create_empty_plot()

    def get_max_value(self) -> float:
        return max(self.animated_y)

    def get_min_value(self) -> float:
        return min(self.animated_y)

    def get_max_velocity(self) -> float:
        if self.velocity_y:
            return max(self.velocity_y)

    def get_min_velocity(self) -> float:
        if self.velocity_y:
            return min(self.velocity_y)

    def get_max_acceleration(self) -> float:
        if self.acceleration_y:
            return max(self.acceleration_y)

    def get_min_acceleration(self) -> float:
        if self.acceleration_y:
            return min(self.acceleration_y)
