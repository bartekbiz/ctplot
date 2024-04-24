from controls.base.SmallButton import SmallButton


class ApplyButton(SmallButton):
    def __init__(self, window, module, row, col):
        super().__init__(
            window,
            text="Apply",
            command=module.apply
        )
        self.grid(row=row, column=col, padx=10, sticky="ne")

        # Binding Enter key to apply button
        self.bind("<Return>", module.apply)
