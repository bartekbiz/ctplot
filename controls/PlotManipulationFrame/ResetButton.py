from controls.base.SmallButton import SmallButton

class ResetButton(SmallButton):
    def __init__(self, window, module, row, col):
        super().__init__(
            window,
            text="Reset",
            command=module.reset_ranges
        )
        self.grid(row=row, column=col, padx=10, sticky="nw")

