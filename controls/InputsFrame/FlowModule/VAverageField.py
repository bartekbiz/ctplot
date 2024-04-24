from controls.base.TextLabel import TextLabel
from controls.base.TextEntry import TextEntry


class VAverageField:
    def __init__(self,window, module, row):
        self.cross_section_label = VAverageLabel(window, row)
        self.cross_section_display = VAverageDisplay(window, row)

    def update_display(self, text):
        self.cross_section_display.config(text=text)

    def destroy(self):
        self.cross_section_label.destroy()
        self.cross_section_display.destroy()


class VAverageLabel(TextLabel):
    def __init__(self, window, row):
        super().__init__(window, text="V Average", width=12)
        self.grid(row=row, column=0, padx=10, sticky="nw")


class VAverageDisplay(TextLabel):
    def __init__(self, window, row):
        super().__init__(window, text="0", width=10)
        self.grid(row=row, column=1, padx=10, sticky="ne")