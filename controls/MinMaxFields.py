from controls.base.TextLabel import TextLabel
from controls.base.TextEntry import TextEntry


class XMinMaxFields:
    def __init__(self, module, row, text, min_value, max_value):
        self.x_min_label = XMinLabel(module, row, text)
        self.x_min_entry = XMinEntry(module, row, min_value)

        self.x_max_label = XMaxLabel(module, row+1, text)
        self.x_max_entry = XMaxEntry(module, row+1, max_value)

    def destroy(self):
        self.x_min_label.destroy()
        self.x_min_entry.destroy()

        self.x_max_label.destroy()
        self.x_max_entry.destroy()


class YMinMaxFields:
    def __init__(self, module, row, text, min_value, max_value):
        self.y_min_label = YMinLabel(module, row, text)
        self.y_min_entry = YMinEntry(module, row, min_value)

        self.y_max_label = YMaxLabel(module, row+1, text)
        self.y_max_entry = YMaxEntry(module, row+1, max_value)

    def destroy(self):
        self.y_min_label.destroy()
        self.y_min_entry.destroy()

        self.y_max_label.destroy()
        self.y_max_entry.destroy()


class XMinLabel(TextLabel):
    def __init__(self, module, row, text):
        super().__init__(module.app, text=f'Xmin for {text}')
        self.grid(row=row, column=0, padx=10, sticky="nw")


class XMinEntry(TextEntry):
    def __init__(self, module, row, min_value):
        super().__init__(module.app, min_value) # module.plot.x_min
        self.grid(row=row, column=1, padx=10, sticky="ne")


class XMaxLabel(TextLabel):
    def __init__(self, module, row, text):
        super().__init__(module.app, text=f'Xmax for {text}')
        self.grid(row=row, column=0, padx=10, sticky="nw")


class XMaxEntry(TextEntry):
    def __init__(self, module, row, max_value):
        super().__init__(module.app, max_value) # module.plot.x_max
        self.grid(row=row, column=1, padx=10, sticky="ne")


class YMinLabel(TextLabel):
    def __init__(self, module, row, text):
        super().__init__(module.app, text=f'Ymin for {text}')
        self.grid(row=row, column=0, padx=10, sticky="nw")


class YMinEntry(TextEntry):
    def __init__(self, module, row, min_value):
        super().__init__(module.app, min_value)
        self.grid(row=row, column=1, padx=10, sticky="ne")


class YMaxLabel(TextLabel):
    def __init__(self, module, row, text):
        super().__init__(module.app, text=f'Ymax for {text}')
        self.grid(row=row, column=0, padx=10, sticky="nw")


class YMaxEntry(TextEntry):
    def __init__(self, module, row, max_value):
        super().__init__(module.app, max_value)
        self.grid(row=row, column=1, padx=10, sticky="ne")
