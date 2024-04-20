from controls.base.TextLabel import TextLabel
from controls.base.TextEntry import TextEntry


class CrossSectionField:
    def __init__(self, module):
        self.cross_section_label = CrossSectionLabel(module)
        self.cross_section_display = CrossSectionDisplay(module)

    def update_display(self, text):
        self.cross_section_display.config(text=text)

    def destroy(self):
        self.cross_section_label.destroy()
        self.cross_section_display.destroy()


class CrossSectionLabel(TextLabel):
    def __init__(self, module):
        super().__init__(module.app, text="Cross Section", width=12)
        self.grid(row=12, column=0, padx=10, sticky="nw")


class CrossSectionDisplay(TextLabel):
    def __init__(self, module):
        super().__init__(module.app, text="0", width=10)
        self.grid(row=12, column=1, padx=10, sticky="ne")
