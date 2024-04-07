import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


class MainPlot:
    def __init__(self, app, data):
        self.app = app
        self.data = data

        self.canvas = None
        self.toolbar = None

        self.x_min = tk.DoubleVar()
        self.x_max = tk.DoubleVar()
        self.y_min = tk.DoubleVar()
        self.y_max = tk.DoubleVar()

    def create_plot(self):
        print("\nCreating plot...")
        self.close_plot()

        # adding the subplot
        fig, (ax1, ax2, ax3) = plt.subplots(3, 1, constrained_layout=True)
        fig.set_figwidth(6.6)
        fig.set_figheight(6.6)

        ax1.plot(self.data["x"], self.data["y"])
        ax2.plot(self.data["x"], self.data["y"])
        ax3.plot(self.data["x"], self.data["y"])

        # Adding grids to plots
        ax1.grid()
        ax2.grid()
        ax3.grid()

        # separate subplot titles
        ax1.set_title("Wykres x(t)")
        ax2.set_title("Wykres v(t)")
        ax3.set_title("Wykres a(t)")

        ax1.set_ylabel("x [m]")
        ax2.set_ylabel("x [m]")
        ax3.set_ylabel("x [m]")

        # common axis labels
        fig.supxlabel("t [s]")

        # Get the minimum and maximum x-values
        min_x = self.x_min.get()
        max_x = self.x_max.get()

        # minimum and maximum x-values are not the same
        if max_x > min_x:
            # minimum and maximum x-values for the plots
            ax1.set_xlim(left=min_x, right=max_x)
            ax2.set_xlim(left=min_x, right=max_x)
            ax3.set_xlim(left=min_x, right=max_x)

        # Get the minimum and maximum y-values
        min_y = self.y_min.get()
        max_y = self.y_max.get()

        # minimum and maximum y-values are not the same
        if max_y > min_y:
            # minimum and maximum y-values for the plots
            ax1.set_ylim(bottom=min_y, top=max_y)
            ax2.set_ylim(bottom=min_y, top=max_y)
            ax3.set_ylim(bottom=min_y, top=max_y)

        # creating the Tkinter canvas
        # containing the Matplotlib figure
        self.canvas = FigureCanvasTkAgg(fig, master=self.app)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=285, y=16)

        # creating the Matplotlib toolbar
        self.toolbar = NavigationToolbar2Tk(self.canvas, self.app, pack_toolbar=False)
        self.toolbar.update()
        self.toolbar.place(x=8, y=self.app.w_height - 40)

        self.app.is_button_disabled = tk.NORMAL
        self.app.close_button.config(state=self.app.is_button_disabled)

    def close_plot(self):
        # Check if the canvas and toolbar exist
        if (self.canvas is not None and
                self.toolbar is not None):
            print("Closing plot...")

            # Destroy the canvas and toolbar
            self.canvas.get_tk_widget().destroy()
            self.toolbar.destroy()
            self.canvas = None
            self.toolbar = None

        self.app.is_button_disabled = tk.DISABLED
        # Update the state of the close_button
        self.app.close_button.config(state=self.app.is_button_disabled)
