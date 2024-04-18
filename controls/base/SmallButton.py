import tkinter as tk


class SmallButton(tk.Button):
    def __init__(self, window, text, command, state=tk.NORMAL):
        super().__init__(
            window,
            text=text,
            command=command,
            font=("Arial", 12, "bold"),
            width=6,
            height=2,
            state=state
        )
