from controls.base.TextLabel import TextLabel
from controls.base.TextEntry import TextEntry


class SpanField:
    def __init__(self, window, module, row):
        self.span_label = SpanLabel(window, row)
        self.span_entry = SpanEntry(window, module, row)

    def destroy(self):
        self.span_label.destroy()
        self.span_entry.destroy()


class SpanLabel(TextLabel):
    def __init__(self, window, row):
        super().__init__(window, text="Span")
        self.grid(row=row, column=0, padx=10, sticky="nw")


class SpanEntry(TextEntry):
    def __init__(self, window, module, row):
        super().__init__(window, module.plot.custom_span)
        self.grid(row=row, column=1, padx=10, sticky="ne")

