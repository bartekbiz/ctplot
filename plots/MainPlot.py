import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class MainPlot:
    def __init__(self, app, data):
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
        # X min/max for the 1 plot
        x_min = self.x_min.get()
        x_max = self.x_max.get()
        self.set_x_min_max_values_ax1(x_min, x_max)

        # Y min/max for the 1 plot
        y_min = self.y_min.get()
        y_max = self.y_max.get()
        self.set_y_min_max_values_ax1(y_min, y_max)


        # X min/max for the 2 plot
        x_min_2 = self.x_min_2.get()
        x_max_2 = self.x_max_2.get()
        self.set_x_min_max_values_ax2(x_min_2, x_max_2)

        # Y min/max for the 2 plot
        y_min_2 = self.y_min_2.get()
        y_max_2 = self.y_max_2.get()
        self.set_y_min_max_values_ax2(y_min_2, y_max_2)

        # X min/max for the 3 plot
        x_min_3 = self.x_min_3.get()
        x_max_3 = self.x_max_3.get()
        self.set_x_min_max_values_ax3(x_min_3, x_max_3)

        # Y min/max for the 3 plot
        y_min_3 = self.y_min_3.get()
        y_max_3 = self.y_max_3.get()
        self.set_y_min_max_values_ax3(y_min_3, y_max_3)




    # setting x min/max values
    def set_x_min_max_values_ax1(self, x_min, x_max):
        if x_min < x_max:
            self.ax1.set_xlim(left=x_min, right=x_max)

    def set_x_min_max_values_ax2(self, x_min_2, x_max_2):
        if x_min_2 < x_max_2:
            self.ax2.set_xlim(left=x_min_2, right=x_max_2)

    def set_x_min_max_values_ax3(self, x_min_3, x_max_3):
        if x_min_3 < x_max_3:
            self.ax3.set_xlim(left=x_min_3, right=x_max_3)

    # setting y min/max values
    def set_y_min_max_values_ax1(self, y_min, y_max):
        if y_min < y_max:
            self.ax1.set_ylim(bottom=y_min, top=y_max)

    def set_y_min_max_values_ax2(self, y_min_2, y_max_2):
        if y_min_2 < y_max_2:
            self.ax2.set_ylim(bottom=y_min_2, top=y_max_2)

    def set_y_min_max_values_ax3(self, y_min_3, y_max_3):
        if y_min_3 < y_max_3:
            self.ax3.set_ylim(bottom=y_min_3, top=y_max_3)


    # def set_x_min_max_values(self, x_min, x_max):
    #     self.ax1.set_xlim(left=x_min, right=x_max)
    #     self.ax2.set_xlim(left=x_min, right=x_max)
    #     self.ax3.set_xlim(left=x_min, right=x_max)

    # def set_y_min_max_values(self, y_min, y_max):
    #     self.ax1.set_ylim(bottom=y_min, top=y_max)
    #     self.ax2.set_ylim(bottom=y_min, top=y_max)
    #     self.ax3.set_ylim(bottom=y_min, top=y_max)

    def set_span_value(self):
        if self.custom_span.get() < 1:
            return

        self.span = self.custom_span.get()

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
