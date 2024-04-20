from controls.base.TextLabel import TextLabel
from controls.base.TextEntry import TextEntry


class DiameterField:
    def __init__(self, module):
        self.span_label = DiameterLabel(module)
        self.span_entry = DiameterEntry(module)


class DiameterLabel(TextLabel):
    def __init__(self, module):
        super().__init__(module.app, text="Diameter")
        self.grid(row=10, column=0, padx=10, sticky="nw")


class DiameterEntry(TextEntry):
    def __init__(self, module):
        super().__init__(module.app, module.plot.custom_span)
        self.grid(row=10, column=1, padx=10, sticky="ne")
