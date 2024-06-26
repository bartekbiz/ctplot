from controls.base.TextEntry import TextEntry
from controls.base.TextLabel import TextLabel


class SpanField:
    def __init__(self, window, module, row, start_col=0):
        self.span_label = SpanLabel(window, row, start_col)
        self.span_entry = SpanEntry(window, module, row, start_col + 1)

    def destroy(self):
        self.span_label.destroy()
        self.span_entry.destroy()


class SpanLabel(TextLabel):
    def __init__(self, window, row, col):
        super().__init__(window, text="Span")
        self.grid(row=row, column=col, padx=10, sticky="nw")


class SpanEntry(TextEntry):
    def __init__(self, window, module, row, col):
        super().__init__(window, module.plot.custom_span)
        self.grid(row=row, column=col, padx=10, sticky="ne")
