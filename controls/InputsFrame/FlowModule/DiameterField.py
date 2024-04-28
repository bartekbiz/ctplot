from controls.base.TextLabel import TextLabel
from controls.base.TextEntry import TextEntry


class DiameterField:
    def __init__(self, window, module, row):
        self.diameter_label = DiameterLabel(window, row)
        self.diameter_entry = DiameterEntry(window, module, row)

    def destroy(self):
        self.diameter_label.destroy()
        self.diameter_entry.destroy()


class DiameterLabel(TextLabel):
    def __init__(self, window, row):
        super().__init__(window, text="Diameter")
        self.grid(row=row, column=0, padx=10, sticky="nw")


class DiameterEntry(TextEntry):
    def __init__(self, window, module, row):
        super().__init__(window, module.diameter_entry)
        self.grid(row=row, column=1, padx=10, sticky="ne")
        self.bind("<FocusOut>", module.update_cross_section)
        self.bind("<Return>", module.update_cross_section)
