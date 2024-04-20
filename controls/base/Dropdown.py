import tkinter as tk


class Dropdown(tk.OptionMenu):
    def __init__(self, app, selected_option, all_options: list):
        super().__init__(
            app,
            selected_option,
            *all_options
        )
