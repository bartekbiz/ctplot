import tkinter as tk


class TextLabel(tk.Label):
    def __init__(self, window, text, width=5):
        super().__init__(
            window,
            text=text,
            font=("Arial", 12, "bold"),
            width=width,
            justify="center",
            relief="solid",
            bd=1,
            bg="white",
            fg="black",
            highlightthickness=2,
        )
