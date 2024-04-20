from controls.base.SmallButton import SmallButton


class ApplyButton(SmallButton):
    def __init__(self, module):
        super().__init__(
            module.app,
            text="Apply",
            command=module.apply
        )
        self.grid(row=9, column=1, padx=10, sticky="ne")

        # Binding Enter key to apply button
        self.bind("<Return>", module.apply)
