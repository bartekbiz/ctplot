from controls.base.TextLabel import TextLabel
from controls.base.TextEntry import TextEntry


class XMinMaxFields:
    def __init__(self, module):
        self.x_min_label = XMinLabel(module)
        self.x_min_entry = XMinEntry(module)

        self.x_max_label = XMaxLabel(module)
        self.x_max_entry = XMaxEntry(module)


class YMinMaxFields:
    def __init__(self, module):
        self.y_min_label = YMinLabel(module)
        self.y_min_entry = YMinEntry(module)

        self.y_max_label = YMaxLabel(module)
        self.y_max_entry = YMaxEntry(module)


class XMinLabel(TextLabel):
    def __init__(self, module):
        super().__init__(module.app, text='Xmin')
        self.grid(row=4, column=0, padx=10, sticky="nw")


class XMinEntry(TextEntry):
    def __init__(self, module):
        super().__init__(module.app, module.plot.x_min)
        self.grid(row=4, column=1, padx=10, sticky="ne")


class XMaxLabel(TextLabel):
    def __init__(self, module):
        super().__init__(module.app, text='Xmax')
        self.grid(row=5, column=0, padx=10, sticky="nw")


class XMaxEntry(TextEntry):
    def __init__(self, module):
        super().__init__(module.app, module.plot.x_max)
        self.grid(row=5, column=1, padx=10, sticky="ne")


class YMinLabel(TextLabel):
    def __init__(self, module):
        super().__init__(module.app, text='Ymin')
        self.grid(row=6, column=0, padx=10, sticky="nw")


class YMinEntry(TextEntry):
    def __init__(self, module):
        super().__init__(module.app, module.plot.y_min)
        self.grid(row=6, column=1, padx=10, sticky="ne")


class YMaxLabel(TextLabel):
    def __init__(self, module):
        super().__init__(module.app, text='Ymax')
        self.grid(row=7, column=0, padx=10, sticky="nw")


class YMaxEntry(TextEntry):
    def __init__(self, module):
        super().__init__(module.app, module.plot.y_max)
        self.grid(row=7, column=1, padx=10, sticky="ne")
