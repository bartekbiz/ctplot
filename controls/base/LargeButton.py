import tkinter as tk


class LargeButton(tk.Button):
    def __init__(self, window, text, command, state=tk.NORMAL):
        super().__init__(
            window,
            text=text,
            command=command,
            font=("Arial", 15, "bold"),
            width=17,
            height=2,
            state=state
        )
