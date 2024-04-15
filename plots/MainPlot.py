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

        self.custom_span = tk.IntVar()
        self.custom_span.set(30)

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
