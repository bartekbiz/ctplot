from tkinter import ttk


class Separator(ttk.Separator):
    def __init__(self, app, row, col):
        super().__init__(app, orient="horizontal")
        self.grid(row=row, column=col, columnspan=2, padx=10, pady=10, sticky="ew")
