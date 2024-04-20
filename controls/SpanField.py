from controls.base.TextLabel import TextLabel
from controls.base.TextEntry import TextEntry


class SpanField:
    def __init__(self, module):
        self.span_label = SpanLabel(module)
        self.span_entry = SpanEntry(module)


class SpanLabel(TextLabel):
    def __init__(self, module):
        super().__init__(module.app, text="Span")
        self.grid(row=8, column=0, padx=10, sticky="nw")


class SpanEntry(TextEntry):
    def __init__(self, module):
        super().__init__(module.app, module.plot.custom_span)
        self.grid(row=8, column=1, padx=10, sticky="ne")
