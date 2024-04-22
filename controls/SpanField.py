from controls.base.TextLabel import TextLabel
from controls.base.TextEntry import TextEntry


class SpanField:
    def __init__(self, module, row):
        self.span_label = SpanLabel(module, row)
        self.span_entry = SpanEntry(module, row)

    def destroy(self):
        self.span_label.destroy()
        self.span_entry.destroy()


class SpanLabel(TextLabel):
    def __init__(self, module, row):
        super().__init__(module.app, text="Span")
        self.grid(row=row, column=0, padx=10, sticky="nw")

        


class SpanEntry(TextEntry):
    def __init__(self, module, row):
        super().__init__(module.app, module.plot.custom_span)
        self.grid(row=row, column=1, padx=10, sticky="ne")

