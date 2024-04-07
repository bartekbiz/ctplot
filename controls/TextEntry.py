import tkinter as tk


class TextEntry(tk.Entry):
    def __init__(self, window, textvariable):
        super().__init__(
            window,
            textvariable=textvariable,
            font=("calibre", 10, "normal"),
            width=10,
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
