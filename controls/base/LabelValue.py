from controls.base.TextLabel import TextLabel


class LabelValue():
    def __init__(self, window, text, row, column):
        self.label = TextLabel(window, text, width=15)
        self.label.grid(row=row, column=column, padx=10, sticky="nw")
        self.value = TextLabel(window, 0)
        self.value.grid(row=row, column=column+1, padx=10, sticky="ne")

    def update_value(self, value: float):
        value = str(round(value, 2))
        self.value.config(text=value)
        
    def destroy(self):
        self.label.destroy()
        self.value.destroy()