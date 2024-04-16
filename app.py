import sys
import tkinter as tk
from tkinter import filedialog
import csv

from controls.LargeButton import LargeButton
from controls.SmallButton import SmallButton
from controls.TextEntry import TextEntry
from controls.TextLabel import TextLabel
import controls.MinMaxFields

from plots.AnimatedPlot import AnimatedPlot
from plots.MainPlot import MainPlot


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("CTPlot")
        self.create_window()

        # Plot fields
        self.data = {"x": [], "y": []}

        self.plot = AnimatedPlot(self)

        # Open CSV Button
        self.open_button = None
        self.create_open_csv_button()
        self.create_open_csv_label()

        # Close button
        self.close_button = None
        self.create_close_plot_button()
        
        # Apply button
        self.apply_button = None
        self.create_apply_button()

        # Input fields
        self.create_x_minmax_field()
        self.create_y_minmax_field()

        self.create_custom_span()
    
        self.add_bindings()

        self.add_close_protocol()

    def create_window(self):
        self.w_width = 960
        self.w_height = 720
        self.geometry(f"{self.w_width}x{self.w_height}")
        self.resizable(width=False, height=False)

    def add_bindings(self):
        # Return key reloads graph
        self.bind("<Return>", self.apply)

        # Escape key closes app
        self.bind("<Escape>", self.destroy_app)
    
    def add_close_protocol(self):
        self.protocol("WM_DELETE_WINDOW", self.destroy_app)

    def create_open_csv_label(self):
        label = tk.Label(self, text="Open CSV file to plot data", font=("Arial", 15))
        label.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nw")

    def create_open_csv_button(self):
        self.open_button = LargeButton(
            self,
            text="Open CSV File",
            command=self.open_csv_file
        )
        self.open_button.grid(row=1, column=0, columnspan=2, padx=10, sticky="nw")
        self.open_button.focus()
        self.open_button.bind("<Return>", self.open_csv_file)

    def create_close_plot_button(self):
        self.is_button_disabled = tk.DISABLED
        self.close_button = LargeButton(
            self,
            text="Close Plot",
            command=self.plot.close_plot,
            state=self.is_button_disabled
        )
        self.close_button.grid(row=2, column=0, columnspan=2, padx=10, sticky="nw")

    def create_x_minmax_field(self):
        controls.MinMaxFields.create_x_minmax_field(self)

    def create_y_minmax_field(self):
        controls.MinMaxFields.create_y_minmax_field(self)

    def create_custom_span(self):
        # span label
        span_label = TextLabel(self, text="Span")
        span_label.grid(row=7, column=0, padx=10, sticky="nw")

        # span input
        span_enter = TextEntry(self, self.plot.custom_span)
        span_enter.grid(row=7, column=1, padx=10, sticky="ne")

    def create_apply_button(self):
        self.apply_button = SmallButton(
            self,
            text="Apply",
            command=self.apply
        )
        self.apply_button.grid(row=8, column=1, padx=10, sticky="ne")

        #Binding Enter key to apply button
        self.apply_button.bind("<Return>", self.apply)

    def apply(self, *event):
        self.plot.create_plot()

    def open_csv_file(self, *event):
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
                        self.data["y"].append(float(row[1])/1000)

                self.plot.create_plot()

                self.is_button_disabled = tk.NORMAL
                # Update the state of the close_button
                self.close_button.config(state=self.is_button_disabled)

            except Exception as e:
                print(f"Error: {e}")

    def destroy_app(self, *event):
        print("\nQuitting...")
        self.destroy()
        sys.exit()
