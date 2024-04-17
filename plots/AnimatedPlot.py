from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import tkinter as tk
from plots.MainPlot import MainPlot
from plots.PlotCalculations import PlotCalculations


class AnimatedPlot(MainPlot):
    def __init__(self, app):
        super().__init__(app)

        self.animation = None
        self.animated_x = []
        self.animated_y = []

        self.velocity = []
        self.acceleration = []

        self.counter = 0
        self.refresh_rate = 40

    def create_plot(self):
        print("\nCreating plot...")
        self.close_plot()

        self.create_figure()

        self.set_plots_props()

        self.update_ax1_data()
        self.update_ax2_ax3_data()

        self.set_min_max_values()

        self.create_canvas()
        self.create_toolbar()

        self.animation = FuncAnimation(self.fig, self.update_frame, interval=5, save_count=60)

        self.update_close_button_state(tk.NORMAL)

    def create_figure(self):
        self.fig, (self.ax1, self.ax2, self.ax3) = plt.subplots(3, 1, constrained_layout=True)

        self.fig.set_figwidth(6.6)
        self.fig.set_figheight(6.6)

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
        self.ax1.plot(self.animated_x, self.animated_y, 'Green')

    def update_ax2_ax3_data(self):
        plot_calculations = PlotCalculations()

        v_x, self.velocity = plot_calculations.calc_linear_regression(self.animated_x, self.animated_y, self.custom_span.get())
        a_x, self.acceleration = plot_calculations.calc_linear_regression(v_x, self.velocity, self.custom_span.get())

        self.ax2.plot(v_x, self.velocity, 'Green')
        self.ax3.plot(a_x, self.acceleration, 'Green')

    def update_frame(self, frame):
        self.animated_x.append(self.app.data["x"][self.counter])
        self.animated_y.append(self.app.data["y"][self.counter])

        self.update_ax1_data()
        if self.counter % self.refresh_rate == 0:
            self.update_ax2_ax3_data()

        self.counter += 1

        return self.ax1, self.ax2, self.ax3

    def close_plot(self):
        if self.canvas is None and self.toolbar is None:
            return

        print("Closing plot...")
        self.canvas.get_tk_widget().destroy()
        self.toolbar.destroy()
        self.canvas = None
        self.toolbar = None

        self.animated_x = []
        self.animated_y = []

        self.update_close_button_state(tk.DISABLED)

    def get_max_value(self) -> float:
        return max(self.animated_y)

    def get_min_value(self) -> float:
        return min(self.animated_y)

    def get_max_velocity(self) -> float:
        if self.velocity:
            return max(self.velocity)

    def get_min_velocity(self) -> float:
        if self.velocity:
            return min(self.velocity)

    def get_max_acceleration(self) -> float:
        if self.acceleration:
            return max(self.acceleration)

    def get_min_acceleration(self) -> float:
        if self.acceleration:
            return min(self.acceleration)
