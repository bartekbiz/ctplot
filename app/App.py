import sys
import tkinter as tk

from modules.BaseModule import BaseModule
from modules.DisplacementModule.DisplacementModule import DisplacementModule
from enums.ModuleEnum import ModuleEnum
from modules.ModuleFactory import ModuleFactory

from controls.base.Frame import Frame
from controls.ModuleFrame.ModuleFrame import ModuleFrame


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window
        self.title("CTPlot")
        self.w_width = 1080
        self.w_height = 720
        self.create_window()

        # Define main app columns
        self.column_0_frame = Frame(self, row=0, col=0)
        self.column_1_frame = Frame(self, row=0, col=1)
        self.column_2_frame = Frame(self, row=0, col=2)

        # Modules
        self.current_module: BaseModule = DisplacementModule(self)
        self.default_module = self.current_module.get_name()

        self.module_frame = ModuleFrame(self)

        # Functional
        self.add_bindings()
        self.add_close_protocol()

    def create_window(self):
        self.geometry(f"{self.w_width}x{self.w_height}")
        self.resizable(width=False, height=False)

    def change_current_module(self, *args):
        self.current_module.destroy()

        # Make new module
        selected_module: ModuleEnum = ModuleEnum.parse_string(self.module_frame.dropdown.selected_module.get())
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
