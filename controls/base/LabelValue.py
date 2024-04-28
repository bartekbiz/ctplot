from controls.base.TextLabel import TextLabel


class LabelValue():
    def __init__(self, window, text, row, col):
        self.label = TextLabel(window, text)
        self.label.grid(row=row, column=col, padx=10, sticky="nw")
        self.value = TextLabel(window, text=0, width=10)
        self.value.grid(row=row, column=col + 1, padx=10, sticky="ne")

    def update_value(self, value: float):
        value = str(round(value, 2))
        self.value.config(text=value)
        
    def destroy(self):
        self.label.destroy()
        self.value.destroy()