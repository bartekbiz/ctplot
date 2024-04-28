from tkinter import Label


class MainLabel(Label):
    def __init__(self, window):
        super().__init__(window, text="Choose calculation mode:", font=("Arial", 15))
        self.grid(row=0, column=0, columnspan=2, padx=10, pady=7, sticky="nw")
