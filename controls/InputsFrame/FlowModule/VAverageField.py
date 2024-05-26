from controls.base.TextEntry import TextEntry
from controls.base.TextLabel import TextLabel


class VAverageField:
    def __init__(self, window, module, row):
        self.v_average_label = VAverageLabel(window, row)
        self.v_average_entry = VAverageEntry(window, module, row)

    def destroy(self):
        self.v_average_label.destroy()
        self.v_average_entry.destroy()


class VAverageLabel(TextLabel):
    def __init__(self, window, row):
        super().__init__(window, text=" VAverage")
        self.grid(row=row, column=0, padx=10, sticky="nw")


class VAverageEntry(TextEntry):
    def __init__(self, window, module, row):
        super().__init__(window, module.v_average_entry)
        self.grid(row=row, column=1, padx=10, sticky="ne")
        self.bind("<FocusOut>", module.update_flow)
        self.bind("<Return>", module.update_flow)
