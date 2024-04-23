from controls.base.TextLabel import TextLabel
from controls.base.TextEntry import TextEntry
from controls.base.Separator import Separator


class MinMaxFields:
    def __init__(self, window, module, start_row, start_col=0):
        self.sep_0 = Separator(window, row=start_row, col=start_col)

        self.x_minmax_fields_1 = XMinMaxFields(
            window,
            start_row=start_row + 1,
            start_col=start_col,
            text=module.plot_1_y_title,
            min_value=module.plot.x_min,
            max_value=module.plot.x_max
        )
        self.y_minmax_fields_1 = YMinMaxFields(
            window,
            start_row=start_row + 3,
            start_col=start_col,
            text=module.plot_1_y_title,
            min_value=module.plot.y_min,
            max_value=module.plot.y_max
        )

        self.sep_1 = Separator(window, row=start_row+5, col=start_col)

        self.x_minmax_fields_2 = XMinMaxFields(
            window,
            start_row=start_row + 6,
            start_col=start_col,
            text=module.plot_2_y_title,
            min_value=module.plot.x_min_2,
            max_value=module.plot.x_max_2
        )
        self.y_minmax_fields_2 = YMinMaxFields(
            window,
            start_row=start_row + 8,
            start_col=start_col,
            text=module.plot_2_y_title,
            min_value=module.plot.y_min_2,
            max_value=module.plot.y_max_2
        )

        self.sep_2 = Separator(window, row=start_row+10, col=start_col)

        self.x_minmax_fields_3 = XMinMaxFields(
            window,
            start_row=start_row + 11,
            start_col=start_col,
            text=module.plot_3_y_title,
            min_value=module.plot.x_min_3,
            max_value=module.plot.x_max_3
        )
        self.y_minmax_fields_3 = YMinMaxFields(
            window,
            start_row=start_row + 13,
            start_col=start_col,
            text=module.plot_3_y_title,
            min_value=module.plot.y_min_3,
            max_value=module.plot.y_max_3
        )

        self.sep_3 = Separator(window, row=start_row+15, col=start_col)

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
    def __init__(self, module, start_row, start_col, text, min_value, max_value):
        self.x_min_label = XMinLabel(module, start_row, start_col, text)
        self.x_min_entry = XMinEntry(module, start_row, start_col+1, min_value)

        self.x_max_label = XMaxLabel(module, start_row + 1, start_col, text)
        self.x_max_entry = XMaxEntry(module, start_row + 1, start_col+1, max_value)

    def destroy(self):
        self.x_min_label.destroy()
        self.x_min_entry.destroy()

        self.x_max_label.destroy()
        self.x_max_entry.destroy()


class YMinMaxFields:
    def __init__(self, window, start_row, start_col, text, min_value, max_value):
        self.y_min_label = YMinLabel(window, start_row, start_col, text)
        self.y_min_entry = YMinEntry(window, start_row, start_col + 1, min_value)

        self.y_max_label = YMaxLabel(window, start_row + 1, start_col, text)
        self.y_max_entry = YMaxEntry(window, start_row + 1, start_col + 1, max_value)

    def destroy(self):
        self.y_min_label.destroy()
        self.y_min_entry.destroy()

        self.y_max_label.destroy()
        self.y_max_entry.destroy()


class XMinLabel(TextLabel):
    def __init__(self, window, row, col, text):
        super().__init__(window, text=f'Xmin for {text}')
        self.grid(row=row, column=col, padx=10, sticky="nw")


class XMinEntry(TextEntry):
    def __init__(self, window, row, col, min_value):
        super().__init__(window, min_value)
        self.grid(row=row, column=col, padx=10, sticky="ne")


class XMaxLabel(TextLabel):
    def __init__(self, window, row, col, text):
        super().__init__(window, text=f'Xmax for {text}')
        self.grid(row=row, column=col, padx=10, sticky="nw")


class XMaxEntry(TextEntry):
    def __init__(self, window, row, col, max_value):
        super().__init__(window, max_value)
        self.grid(row=row, column=col, padx=10, sticky="ne")


class YMinLabel(TextLabel):
    def __init__(self, window, row, col, text):
        super().__init__(window, text=f'Ymin for {text}')
        self.grid(row=row, column=col, padx=10, sticky="nw")


class YMinEntry(TextEntry):
    def __init__(self, window, row, col, min_value):
        super().__init__(window, min_value)
        self.grid(row=row, column=col, padx=10, sticky="ne")


class YMaxLabel(TextLabel):
    def __init__(self, window, row, col, text):
        super().__init__(window, text=f'Ymax for {text}')
        self.grid(row=row, column=col, padx=10, sticky="nw")


class YMaxEntry(TextEntry):
    def __init__(self, window, row, col, max_value):
        super().__init__(window, max_value)
        self.grid(row=row, column=col, padx=10, sticky="ne")

    