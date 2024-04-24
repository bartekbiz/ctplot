from controls.base.TextLabel import TextLabel
from controls.base.TextEntry import TextEntry


class CrossSectionField:
    def __init__(self,window, module, row):
        self.cross_section_label = CrossSectionLabel(window, row)
        self.cross_section_display = CrossSectionDisplay(window, row)

    def update_display(self, text):
        self.cross_section_display.config(text=text)

    def destroy(self):
        self.cross_section_label.destroy()
        self.cross_section_display.destroy()


class CrossSectionLabel(TextLabel):
    def __init__(self, window, row):
        super().__init__(window, text="Cross Section")
        self.grid(row=row, column=0, padx=10, sticky="nw")


class CrossSectionDisplay(TextLabel):
    def __init__(self, window, row):
        super().__init__(window, text="0", width=10)
        self.grid(row=row, column=1, padx=10, sticky="ne")
