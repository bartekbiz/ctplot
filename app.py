import tkinter as tk
from tkinter import filedialog
import csv

from controls.LargeButton import LargeButton
from controls.SmallButton import SmallButton
from controls.TextEntry import TextEntry
from controls.TextLabel import TextLabel

from plots.MainPlot import MainPlot


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

        self.is_button_disabled = tk.DISABLED

        # Create label
        label = tk.Label(self, text="Open CSV file to plot data", font=("Arial", 15))
        label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nw")

        self.plot = MainPlot(self)

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
            command=self.plot.close_plot,
            state=self.is_button_disabled
        )
        self.close_button.grid(row=2, column=0, columnspan=2, padx=10, sticky="nw")

    def create_x_minmax(self):
        # Xmin label field
        x_min_label = TextLabel(self, text='Xmin')
        x_min_label.grid(row=3, column=0, padx=10, sticky="nw")

        # Xmin input field
        x_min_enter = TextEntry(self, self.plot.x_min)
        x_min_enter.grid(row=3, column=1, padx=10, sticky="ne")

        # Xmax label field
        x_max_label = TextLabel(self, text='Xmax')
        x_max_label.grid(row=4, column=0, padx=10, sticky="nw")

        # Xmax input field
        x_max_enter = TextEntry(self, self.plot.x_max)
        x_max_enter.grid(row=4, column=1, padx=10, sticky="ne")

    def create_y_minmax(self):
        # Ymin label field
        y_min_label = TextLabel(self, text='Ymin')
        y_min_label.grid(row=5, column=0, padx=10, sticky="nw")

        # Ymin input field
        y_min_enter = TextEntry(self, self.plot.y_min)
        y_min_enter.grid(row=5, column=1, padx=10, sticky="ne")

        # Ymax label field
        y_max_label = TextLabel(self, text='Ymax')
        y_max_label.grid(row=6, column=0, padx=10, sticky="nw")

        # Ymax input field
        y_max_enter = TextEntry(self, self.plot.y_max)
        y_max_enter.grid(row=6, column=1, padx=10, sticky="ne")

    def create_apply_button(self):
        self.apply_button = SmallButton(
            self,
            text="Apply",
            command=self.plot.create_plot
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

                self.plot.create_plot()

                self.is_button_disabled = tk.NORMAL
                # Update the state of the close_button
                self.close_button.config(state=self.is_button_disabled)

            except Exception as e:
                print(f"Error: {e}")

    def destroy_app(self):
        print("\nQuitting...")
        self.destroy()
        exit()
