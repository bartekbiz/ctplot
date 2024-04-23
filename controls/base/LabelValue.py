from controls.base.TextLabel import TextLabel


class LabelValue():
    def __init__(self, window, text, row, column):
        self.label = TextLabel(window, text)
        self.label.grid(row=row, column=column, padx=10, sticky="nw")
        self.value = TextLabel(window, 0)
        self.value.grid(row=row, column=column+1, padx=10, sticky="ne")

    def update_value(self, value):
        self.value.config(text=value)
        
    def destroy(self):
        self.label.destroy()
        self.value.destroy()