from controls.base.SmallButton import SmallButton


def create_apply_button(self):
    self.apply_button = SmallButton(
        self.app,
        text="Apply",
        command=self.apply
    )
    self.apply_button.grid(row=9, column=1, padx=10, sticky="ne")

    # Binding Enter key to apply button
    self.apply_button.bind("<Return>", self.apply)
