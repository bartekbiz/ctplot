from controls.base.TextLabel import TextLabel
from controls.base.TextEntry import TextEntry


class XMinMaxFields:
    def __init__(self, module, row):
        self.x_min_label = XMinLabel(module, row)
        self.x_min_entry = XMinEntry(module, row)

        self.x_max_label = XMaxLabel(module, row)
        self.x_max_entry = XMaxEntry(module, row)

    def destroy(self):
        self.x_min_label.destroy()
        self.x_min_entry.destroy()

        self.x_max_label.destroy()
        self.x_max_entry.destroy()


class YMinMaxFields:
    def __init__(self, module, row):
        self.y_min_label = YMinLabel(module, row)
        self.y_min_entry = YMinEntry(module, row)

        self.y_max_label = YMaxLabel(module, row)
        self.y_max_entry = YMaxEntry(module, row)

    def destroy(self):
        self.y_min_label.destroy()
        self.y_min_entry.destroy()

        self.y_max_label.destroy()
        self.y_max_entry.destroy()


class XMinLabel(TextLabel):
    def __init__(self, module, row):
        super().__init__(module.app, text='Xmin')
        self.grid(row=row, column=0, padx=10, sticky="nw")


class XMinEntry(TextEntry):
    def __init__(self, module, row):
        super().__init__(module.app, module.plot.x_min)
        self.grid(row=row, column=1, padx=10, sticky="ne")


class XMaxLabel(TextLabel):
    def __init__(self, module, row):
        super().__init__(module.app, text='Xmax')
        self.grid(row=row, column=0, padx=10, sticky="nw")


class XMaxEntry(TextEntry):
    def __init__(self, module, row):
        super().__init__(module.app, module.plot.x_max)
        self.grid(row=row, column=1, padx=10, sticky="ne")


class YMinLabel(TextLabel):
    def __init__(self, module, row):
        super().__init__(module.app, text='Ymin')
        self.grid(row=row, column=0, padx=10, sticky="nw")


class YMinEntry(TextEntry):
    def __init__(self, module, row):
        super().__init__(module.app, module.plot.y_min)
        self.grid(row=row, column=1, padx=10, sticky="ne")


class YMaxLabel(TextLabel):
    def __init__(self, module, row):
        super().__init__(module.app, text='Ymax')
        self.grid(row=row, column=0, padx=10, sticky="nw")


class YMaxEntry(TextEntry):
    def __init__(self, module, row):
        super().__init__(module.app, module.plot.y_max)
        self.grid(row=row, column=1, padx=10, sticky="ne")
