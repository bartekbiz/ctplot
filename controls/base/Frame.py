import tkinter as tk


class Frame(tk.Frame):
    def __init__(self, window, row, col=0, rowspan=1, colspan=1, sticky="nw"):
        super().__init__(window)
        self.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, sticky=sticky)
