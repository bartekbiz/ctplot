from controls.base.TextLabel import TextLabel
from controls.base.TextEntry import TextEntry
from controls.base.Separator import Separator


class MinMaxFields:
    def __init__(self, module):
        self.x_minmax_fields_1 = XMinMaxFields(
            module, row=5, text=module.plot_1_y_title, min_value=module.plot.x_min, max_value=module.plot.x_max)
        self.y_minmax_fields_1 = YMinMaxFields(
            module, row=7, text=module.plot_1_y_title, min_value=module.plot.y_min, max_value=module.plot.y_max)
        self.sep_1 = Separator(module.app, row=9)

        self.x_minmax_fields_2 = XMinMaxFields(
            module, row=10, text=module.plot_2_y_title, min_value=module.plot.x_min_2, max_value=module.plot.x_max_2)
        self.y_minmax_fields_2 = YMinMaxFields(
            module, row=12, text=module.plot_2_y_title, min_value=module.plot.y_min_2, max_value=module.plot.y_max_2)
        self.sep_2 = Separator(module.app, row=14)

        self.x_minmax_fields_3 = XMinMaxFields(
            module, row=15, text=module.plot_3_y_title, min_value=module.plot.x_min_3, max_value=module.plot.x_max_3)
        self.y_minmax_fields_3 = YMinMaxFields(
            module, row=17, text=module.plot_3_y_title, min_value=module.plot.y_min_3, max_value=module.plot.y_max_3)
        self.sep_3 = Separator(module.app, row=19)

    def destroy(self):
        self.x_minmax_fields_1.destroy()
        self.y_minmax_fields_1.destroy()
        self.sep_1.destroy()

        self.x_minmax_fields_2.destroy()
        self.y_minmax_fields_2.destroy()
        self.sep_2.destroy()

        self.x_minmax_fields_3.destroy()
        self.y_minmax_fields_3.destroy()
        self.sep_3.destroy()


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
        super().__init__(module.app, min_value)
        self.grid(row=row, column=1, padx=10, sticky="ne")


class XMaxLabel(TextLabel):
    def __init__(self, module, row, text):
        super().__init__(module.app, text=f'Xmax for {text}')
        self.grid(row=row, column=0, padx=10, sticky="nw")


class XMaxEntry(TextEntry):
    def __init__(self, module, row, max_value):
        super().__init__(module.app, max_value)
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

    