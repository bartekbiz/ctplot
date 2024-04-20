import sys
import tkinter as tk

from enums.ModuleEnum import ModuleEnum
from modules.BaseModule import BaseModule
from modules.ModuleFactory import ModuleFactory
from modules.DisplacementModule import DisplacementModule

from app_ui.OpenCSVButton import OpenCSVButton
from app_ui.CloseButton import CloseButton


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("CTPlot")

        # Window
        self.w_width = None
        self.w_height = None
        self.create_window()

        self.create_main_label()

        # Modules
        self.selected_module_str = None
        self.current_module: BaseModule = DisplacementModule(self)
        self.default_module = self.current_module.get_module_name()

        # Calculation mode dropdown menu
        self.dropdown = None
        self.create_module_dropdown()

        self.open_csv_file = OpenCSVButton(self)

        self.close_button = CloseButton(self)
    
        self.add_bindings()

        self.add_close_protocol()

    def create_window(self):
        self.w_width = 960
        self.w_height = 720
        self.geometry(f"{self.w_width}x{self.w_height}")
        self.resizable(width=False, height=False)

    def create_main_label(self):
        label = tk.Label(self, text="Choose calculation mode:", font=("Arial", 17))
        label.grid(row=0, column=0, columnspan=2, padx=10, pady=7, sticky="nw")

    def create_module_dropdown(self):
        all_modules = [i.value for i in ModuleEnum]

        self.selected_module_str = tk.StringVar()
        self.selected_module_str.set(self.default_module.value)

        self.dropdown = tk.OptionMenu(self, self.selected_module_str, *all_modules)
        self.dropdown.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nw")
        self.dropdown.bind("<Button>", self.handle_dropdown_focused)
        self.dropdown.bind("<Return>", self.handle_dropdown_focused)
        self.dropdown.bind("<Leave>", self.handle_dropdown_focused_out)

        self.selected_module_str.trace('w', self.handle_dropdown_changed)

    def handle_dropdown_focused(self, *event):
        self.current_module.plot.pause_plot()

    def handle_dropdown_focused_out(self, *event):
        self.current_module.plot.resume_plot()

    def handle_dropdown_changed(self, *args):
        self.current_module.close_module()

        # Make new module
        selected_module: ModuleEnum = ModuleEnum.parse_string(self.selected_module_str.get())
        self.current_module = ModuleFactory.make_module(selected_module, self)

        print(f"\nCurrent module: {self.current_module.get_module_name()}")

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
