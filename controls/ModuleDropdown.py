import tkinter as tk

from controls.base.Dropdown import Dropdown
from enums.ModuleEnum import ModuleEnum


class ModuleDropdown(Dropdown):
    def __init__(self, window, app):
        self.app = app

        self.selected_module = tk.StringVar()
        self.selected_module.set(self.app.default_module.value)
        self.all_modules = [m.value for m in ModuleEnum]

        super().__init__(window, self.selected_module, self.all_modules)

        self.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nw")
        self.bind("<Button>", self.handle_dropdown_focused)
        self.bind("<Return>", self.handle_dropdown_focused)
        self.bind("<Leave>", self.handle_dropdown_focused_out)

        self.selected_module.trace('w', self.app.change_current_module)

    def handle_dropdown_focused(self, *event):
        self.app.current_module.plot.pause_plot()

    def handle_dropdown_focused_out(self, *event):
        self.app.current_module.plot.resume_plot()
