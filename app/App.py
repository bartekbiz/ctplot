import sys
import tkinter as tk

from modules.BaseModule import BaseModule
from modules.DisplacementModule.DisplacementModule import DisplacementModule
from enums.ModuleEnum import ModuleEnum
from modules.ModuleFactory import ModuleFactory

from controls.MainLabel import MainLabel
from controls.ModuleDropdown import ModuleDropdown


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window
        self.title("CTPlot")
        self.w_width = 960
        self.w_height = 720
        self.create_window()

        # Modules
        self.current_module: BaseModule = DisplacementModule(self)
        self.default_module = self.current_module.get_name()

        # Controls
        MainLabel(self)
        self.dropdown = ModuleDropdown(self)

        # Functional
        self.add_bindings()
        self.add_close_protocol()

    def create_window(self):
        self.geometry(f"{self.w_width}x{self.w_height}")
        self.resizable(width=False, height=False)

    def change_current_module(self, *args):
        self.current_module.destroy()

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
        self.current_module.destroy()
        self.destroy()
        sys.exit()
