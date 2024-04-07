import tkinter as tk
from tkinter import filedialog
import csv
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

from controls.LargeButton import LargeButton
from controls.SmallButton import SmallButton
from controls.TextEntry import TextEntry
from controls.TextLabel import TextLabel


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("CTPlot")

        # window fields
        self.w_width = 960
        self.w_height = 720
        self.geometry(f"{self.w_width}x{self.w_height}")
        self.resizable(width=False, height=False)

        # plot fields
        self.data = {"x": [], "y": []}
        self.canvas = None
        self.toolbar = None
        self.is_button_disabled = tk.DISABLED
        self.x_min = tk.DoubleVar()
        self.x_max = tk.DoubleVar()
        self.y_min = tk.DoubleVar()
        self.y_max = tk.DoubleVar()

        # Create label
        label = tk.Label(self, text="Open CSV file to plot data", font=("Arial", 15))
        label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nw")

        self.open_button = None
        self.create_open_csv_button()

        self.close_button = None
        self.create_close_plot_button()

        self.create_x_minmax()
        self.create_y_minmax()

        self.apply_button = None
        self.create_apply_button()

        self.protocol("WM_DELETE_WINDOW", self.destroy_app)

    def create_open_csv_button(self):
        self.open_button = LargeButton(
            self,
            text="Open CSV File",
            command=self.open_csv_file
        )

        self.open_button.grid(row=1, column=0, columnspan=2, padx=10, sticky="nw")

    def create_close_plot_button(self):
        self.close_button = LargeButton(
            self,
            text="Close Plot",
            command=self.close_plot,
            state=self.is_button_disabled
        )
        self.close_button.grid(row=2, column=0, columnspan=2, padx=10, sticky="nw")

    def create_x_minmax(self):
        # Xmin label field
        x_min_label = TextLabel(self, text='Xmin')
        x_min_label.grid(row=3, column=0, padx=10, sticky="nw")

        # Xmin input field
        x_min_enter = TextEntry(self, self.x_min)
        x_min_enter.grid(row=3, column=1, padx=10, sticky="ne")

        # Xmax label field
        x_max_label = TextLabel(self, text='Xmax')
        x_max_label.grid(row=4, column=0, padx=10, sticky="nw")

        # Xmax input field
        x_max_enter = TextEntry(self, self.x_max)
        x_max_enter.grid(row=4, column=1, padx=10, sticky="ne")

    def create_y_minmax(self):
        # Ymin label field
        y_min_label = TextLabel(self, text='Ymin')
        y_min_label.grid(row=5, column=0, padx=10, sticky="nw")

        # Ymin input field
        y_min_enter = TextEntry(self, self.y_min)
        y_min_enter.grid(row=5, column=1, padx=10, sticky="ne")

        # Ymax label field
        y_max_label = TextLabel(self, text='Ymax')
        y_max_label.grid(row=6, column=0, padx=10, sticky="nw")

        # Ymax input field
        y_max_enter = TextEntry(self, self.y_max)
        y_max_enter.grid(row=6, column=1, padx=10, sticky="ne")

    def create_apply_button(self):
        self.apply_button = tk.Button(
            master=self,
            text="Apply",
            command=self.create_plot,
            font=('calibre', 10, 'normal'),
            width=5
        )
        self.apply_button = SmallButton(
            self,
            text="Apply",
            command=self.create_plot
        )
        self.apply_button.grid(row=7, column=1, padx=10, sticky="ne")

    def open_csv_file(self):
        file_path = filedialog.askopenfilename(
            defaultextension=".csv", filetypes=[("CSV Files", "*.csv")]
        )

        if file_path:
            try:
                with open(file_path, "r") as csv_file:
                    csv_reader = csv.reader(csv_file)
                    self.data["x"].clear()
                    self.data["y"].clear()

                    for row in csv_reader:
                        self.data["x"].append(float(row[0]))
                        self.data["y"].append(float(row[2]))

                self.create_plot()

                self.is_button_disabled = tk.NORMAL
                # Update the state of the close_button
                self.close_button.config(state=self.is_button_disabled)

            except Exception as e:
                print(f"Error: {e}")

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

        self.is_button_disabled = tk.DISABLED
        # Update the state of the close_button
        self.close_button.config(state=self.is_button_disabled)

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
        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=285, y=16)

        # creating the Matplotlib toolbar
        self.toolbar = NavigationToolbar2Tk(self.canvas, self, pack_toolbar=False)
        self.toolbar.update()
        self.toolbar.place(x=8, y=self.w_height - 40)

        self.is_button_disabled = tk.NORMAL
        self.close_button.config(state=self.is_button_disabled)

    def destroy_app(self):
        print("\nQuitting...")
        self.destroy()
        exit()
