import tkinter as tk
from controls.LargeButton import LargeButton


class CloseButton(LargeButton):
    def __init__(self, app):
        self.is_disabled = False
        self.__state = tk.DISABLED

        super().__init__(
            app,
            text="Close Plot",
            command=app.plot.close_plot,
            state=self.__state
        )

        self.grid(row=3, column=0, columnspan=2, padx=10, sticky="nw")

    def set_is_disabled(self, state: bool):
        self.is_disabled = state

        if self.is_disabled:
            self.__state = tk.DISABLED
        else:
            self.__state = tk.NORMAL

        self.config(state=self.__state)
