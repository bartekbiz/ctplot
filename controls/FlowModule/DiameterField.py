from controls.base.TextLabel import TextLabel
from controls.base.TextEntry import TextEntry


class DiameterField:
    def __init__(self, module):
        self.diameter_label = DiameterLabel(module)
        self.diameter_entry = DiameterEntry(module)

    def destroy(self):
        self.diameter_label.destroy()
        self.diameter_entry.destroy()


class DiameterLabel(TextLabel):
    def __init__(self, module):
        super().__init__(module.app, text="Diameter", width=10)
        self.grid(row=10, column=0, padx=10, sticky="nw")


class DiameterEntry(TextEntry):
    def __init__(self, module):
        super().__init__(module.app, module.diameter_entry)
        self.grid(row=10, column=1, padx=10, sticky="ne")
        self.bind("<FocusOut>", module.update_cross_section)
        self.bind("<Return>", module.update_cross_section)
