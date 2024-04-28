import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class MainPlot:
    def __init__(self, window, app, data):
        self.window = window
        self.app = app
        self.data = data

        self.fig = None
        self.ax1 = None
        self.ax2 = None
        self.ax3 = None

        self.color = "Blue"

        self.canvas = None
        self.toolbar = None

        # Ranges for 1st plot
        self.x_min = tk.DoubleVar()
        self.x_max = tk.DoubleVar()
        self.y_min = tk.DoubleVar()
        self.y_max = tk.DoubleVar()

        # Ranges for 2 plot
        self.x_min_2 = tk.DoubleVar()
        self.x_max_2 = tk.DoubleVar()
        self.y_min_2 = tk.DoubleVar()
        self.y_max_2 = tk.DoubleVar()

        # Ranges for 3rd plot
        self.x_min_3 = tk.DoubleVar()
        self.x_max_3 = tk.DoubleVar()
        self.y_min_3 = tk.DoubleVar()
        self.y_max_3 = tk.DoubleVar()

        self.custom_span = tk.IntVar()
        self.custom_span.set(30)
        self.span = None
        self.set_span_value()

    def set_min_max_values(self):
        self.set_axis_limits(self.ax1, self.x_min.get(), self.x_max.get(), self.y_min.get(), self.y_max.get())
        self.set_axis_limits(self.ax2, self.x_min_2.get(), self.x_max_2.get(), self.y_min_2.get(), self.y_max_2.get())
        self.set_axis_limits(self.ax3, self.x_min_3.get(), self.x_max_3.get(), self.y_min_3.get(), self.y_max_3.get())

    def reset_all_ranges(self):
        self.x_min.set(0.0)
        self.x_max.set(0.0)
        self.y_min.set(0.0)
        self.y_max.set(0.0)

        self.x_min_2.set(0.0)
        self.x_max_2.set(0.0)
        self.y_min_2.set(0.0)
        self.y_max_2.set(0.0)

        self.x_min_3.set(0.0)
        self.x_max_3.set(0.0)
        self.y_min_3.set(0.0)
        self.y_max_3.set(0.0)

    @staticmethod
    def set_axis_limits(axis, x_min, x_max, y_min, y_max):
        if x_min < x_max:
            axis.set_xlim(left=x_min, right=x_max)
        if y_min < y_max:
            axis.set_ylim(bottom=y_min, top=y_max)

    def set_span_value(self):
        if self.custom_span.get() < 1:
            return

        self.span = self.custom_span.get()

    def create_canvas(self):
        # creating the Tkinter canvas
        # containing the Matplotlib figure
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.window)
        self.canvas.draw()
        # self.canvas.get_tk_widget().place(x=285, y=16)
        self.canvas.get_tk_widget().grid(row=0, column=0, padx=10, pady=10,sticky="ne")

    def create_toolbar(self):
        # creating the Matplotlib toolbar
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.window, pack_toolbar=False)
        self.toolbar.update()
        self.toolbar.place(x=8, y=self.app.w_height - 40)
