from tkinter import Label


class MainLabel(Label):
    def __init__(self, app):
        super().__init__(app, text="Choose calculation mode:", font=("Arial", 17))
        self.grid(row=0, column=0, columnspan=2, padx=10, pady=7, sticky="nw")
