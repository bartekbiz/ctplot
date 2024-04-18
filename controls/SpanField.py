from controls.base.TextLabel import TextLabel
from controls.base.TextEntry import TextEntry


def create_custom_span(self):
    # span label
    span_label = TextLabel(self.app, text="Span")
    span_label.grid(row=8, column=0, padx=10, sticky="nw")

    # span input
    span_enter = TextEntry(self.app, self.plot.custom_span)
    span_enter.grid(row=8, column=1, padx=10, sticky="ne")
