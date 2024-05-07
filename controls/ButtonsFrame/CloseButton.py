import tkinter as tk

from controls.base.LargeButton import LargeButton


class CloseButton(LargeButton):
    def __init__(self, window, module, row, col=0):
        self.is_disabled = False
        self.__state = tk.DISABLED

        super().__init__(
            window,
            text="Close Plot",
            command=module.plot.close_plot,
            state=self.__state
        )

        self.grid(row=row, column=col, columnspan=2, padx=10, sticky="nw")

    def set_is_disabled(self, state: bool):
        self.is_disabled = state

        if self.is_disabled:
            self.__state = tk.DISABLED
        else:
            self.__state = tk.NORMAL

        self.config(state=self.__state)
