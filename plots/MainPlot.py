import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from plots.PlotCalculations import PlotCalculations


class MainPlot:
    def __init__(self, app):
        self.app = app

        self.fig = None
        self.ax1 = None
        self.ax2 = None
        self.ax3 = None

        self.canvas = None
        self.toolbar = None

        self.x_min = tk.DoubleVar()
        self.x_max = tk.DoubleVar()
        self.y_min = tk.DoubleVar()
        self.y_max = tk.DoubleVar()

    def create_plot(self):
        print("\nCreating plot...")
        self.close_plot()

        self.create_figure()

        self.set_min_max_values()

        self.create_canvas()
        self.create_toolbar()

        self.update_close_button_state(tk.NORMAL)

    def close_plot(self):
        if (self.canvas is not None and
                self.toolbar is not None):
            print("Closing plot...")

            self.canvas.get_tk_widget().destroy()
            self.toolbar.destroy()
            self.canvas = None
            self.toolbar = None

            self.update_close_button_state(tk.DISABLED)

    def create_figure(self):

        # adding the subplot
        self.fig, (self.ax1, self.ax2, self.ax3) = plt.subplots(3, 1, constrained_layout=True)
        self.fig.set_figwidth(6.6)
        self.fig.set_figheight(6.6)

        self.set_single_plot_props(self.ax1, "Wykres x(t)", "x [m]", self.app.data["x"], self.app.data["y"])

        plot_calculations = PlotCalculations()

        v_x, v_y = plot_calculations.calc_linear_regression(self.app.data["x"], self.app.data["y"], 10)
        self.set_single_plot_props(self.ax2, "Wykres v(t)", "v [m/s]", v_x, v_y)

        a_x, a_y = plot_calculations.calc_linear_regression(v_x, v_y, 10)
        self.set_single_plot_props(self.ax3, "Wykres a(t)", "a [m/s*s]", a_x, a_y)

        # common axis labels
        self.fig.supxlabel("t [s]")

    @staticmethod
    def set_single_plot_props(ax, title, y_label, x_data, y_data):
        ax.plot(x_data, y_data)
        ax.set_title(title)
        ax.set_ylabel(y_label)
        ax.grid()

    def set_min_max_values(self):
        x_min = self.x_min.get()
        x_max = self.x_max.get()

        if x_min < x_max:
            self.set_x_min_max_values(x_min, x_max)

        y_min = self.y_min.get()
        y_max = self.y_max.get()

        if y_min < y_max:
            self.set_y_min_max_values(y_min, y_max)

    def set_x_min_max_values(self, x_min, x_max):
        self.ax1.set_xlim(left=x_min, right=x_max)
        self.ax2.set_xlim(left=x_min, right=x_max)
        self.ax3.set_xlim(left=x_min, right=x_max)

    def set_y_min_max_values(self, y_min, y_max):
        self.ax1.set_ylim(bottom=y_min, top=y_max)
        self.ax2.set_ylim(bottom=y_min, top=y_max)
        self.ax3.set_ylim(bottom=y_min, top=y_max)

    def create_canvas(self):
        # creating the Tkinter canvas
        # containing the Matplotlib figure
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.app)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=285, y=16)

    def create_toolbar(self):
        # creating the Matplotlib toolbar
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.app, pack_toolbar=False)
        self.toolbar.update()
        self.toolbar.place(x=8, y=self.app.w_height - 40)

    def update_close_button_state(self, state):
        self.app.is_button_disabled = state
        self.app.close_button.config(state=self.app.is_button_disabled)
