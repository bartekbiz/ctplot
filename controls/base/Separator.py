from tkinter import ttk


class Separator(ttk.Separator):
    def __init__(self, app):
        super().__init__(app, orient="horizontal")
