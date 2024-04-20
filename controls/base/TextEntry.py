import tkinter as tk


class TextEntry(tk.Entry):
    def __init__(self, window, text_variable, width=10):
        super().__init__(
            window,
            textvariable=text_variable,
            font=("Arial", 12, "normal"),
            width=width,
            justify="center",
            relief="solid",
            bd=1,
            bg="white",
            fg="black",
            highlightcolor="blue",
            highlightthickness=1,
            insertbackground="black",
            selectbackground="blue",
            selectforeground="white"
        )
