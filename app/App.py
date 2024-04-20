import sys
import tkinter as tk

from modules.BaseModule import BaseModule
from modules.DisplacementModule import DisplacementModule
from enums.ModuleEnum import ModuleEnum
from modules.ModuleFactory import ModuleFactory

from controls.ModuleDropdown import ModuleDropdown
from controls.OpenCSVButton import OpenCSVButton
from controls.CloseButton import CloseButton


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("CTPlot")

        # Window
        self.w_width = 960
        self.w_height = 720
        self.create_window()

        self.create_main_label()

        # Modules
        self.current_module: BaseModule = DisplacementModule(self)
        self.default_module = self.current_module.get_name()

        # Controls
        self.dropdown = ModuleDropdown(self)

        self.open_csv_file = OpenCSVButton(self)

        self.close_button = CloseButton(self)

        # App bindings
        self.add_bindings()

        self.add_close_protocol()

    def create_window(self):
        self.geometry(f"{self.w_width}x{self.w_height}")
        self.resizable(width=False, height=False)

    def create_main_label(self):
        label = tk.Label(self, text="Choose calculation mode:", font=("Arial", 17))
        label.grid(row=0, column=0, columnspan=2, padx=10, pady=7, sticky="nw")

    def change_current_module(self, *args):
        self.current_module.close()

        # Make new module
        selected_module: ModuleEnum = ModuleEnum.parse_string(self.dropdown.selected_module.get())
        self.current_module = ModuleFactory.make_module(selected_module, self)

        print(f"\nCurrent module: {self.current_module.get_name()}")

    def add_bindings(self):
        # Return key reloads graph
        self.bind("<Return>", self.current_module.apply)

        # Escape key closes app
        self.bind("<Escape>", self.destroy_app)
    
    def add_close_protocol(self):
        self.protocol("WM_DELETE_WINDOW", self.destroy_app)

    def destroy_app(self, *event):
        print("\nQuitting...")
        self.destroy()
        sys.exit()
