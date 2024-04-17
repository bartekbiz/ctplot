import sys
import tkinter as tk

from controls.LargeButton import LargeButton
from controls.SmallButton import SmallButton
from controls.TextEntry import TextEntry
from controls.TextLabel import TextLabel
import controls.MinMaxFields

from enums.ModuleEnum import ModuleEnum
from modules.BaseModule import BaseModule
from modules.ModuleFactory import ModuleFactory
from modules.DisplacementModule import DisplacementModule

from app_ui.OpenCSVFile import OpenCSVFile
from app_ui.CloseButton import CloseButton


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("CTPlot")
        self.create_window()

        self.create_main_label()

        # Plot fields
        self.data = {"x": [], "y": []}

        self.open_csv_file = OpenCSVFile(self)

        # Modules
        self.selected_module = None
        self.default_module = ModuleEnum.displacement
        self.current_module: BaseModule = DisplacementModule(self)

        # Calculation mode dropdown menu
        self.dropdown = None
        self.create_module_dropdown()

        # Open CSV Button
        self.open_button = None
        self.create_open_csv_button()

        # Close button
        self.close_button = CloseButton(self)
        
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

    def create_main_label(self):
        label = tk.Label(self, text="Choose calculation mode:", font=("Arial", 17))
        label.grid(row=0, column=0, columnspan=2, padx=10, pady=7, sticky="nw")

    def create_module_dropdown(self):
        all_modules = [i.value for i in ModuleEnum]

        self.selected_module = tk.StringVar()
        self.selected_module.set(self.default_module.value)

        self.dropdown = tk.OptionMenu(self, self.selected_module, *all_modules)
        self.dropdown.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nw")

        self.selected_module.trace('w', self.change_dropdown)

    def change_dropdown(self, *args):
        print(self.selected_module.get())
        ModuleFactory.make_module(self.selected_module, self)

    def create_open_csv_button(self):
        self.open_button = LargeButton(
            self,
            text="Open CSV File",
            command=self.open_csv_file.open
        )
        self.open_button.grid(row=2, column=0, columnspan=2, padx=10, sticky="nw")
        self.open_button.focus()
        self.open_button.bind("<Return>", self.open_csv_file.open)

    def create_x_minmax_field(self):
        controls.MinMaxFields.create_x_minmax_field(self)

    def create_y_minmax_field(self):
        controls.MinMaxFields.create_y_minmax_field(self)

    def create_custom_span(self):
        # span label
        span_label = TextLabel(self, text="Span")
        span_label.grid(row=8, column=0, padx=10, sticky="nw")

        # span input
        span_enter = TextEntry(self, self.current_module.plot.custom_span)
        span_enter.grid(row=8, column=1, padx=10, sticky="ne")

    def create_apply_button(self):
        self.apply_button = SmallButton(
            self,
            text="Apply",
            command=self.apply
        )
        self.apply_button.grid(row=9, column=1, padx=10, sticky="ne")

        #Binding Enter key to apply button
        self.apply_button.bind("<Return>", self.apply)

    def apply(self, *event):
        self.current_module.plot.create_plot()

    def destroy_app(self, *event):
        print("\nQuitting...")
        self.destroy()
        sys.exit()
