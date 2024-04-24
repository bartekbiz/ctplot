from controls.base.TextLabel import TextLabel
from controls.base.TextEntry import TextEntry


class DeviceRangeField:
    def __init__(self, window, module, start_row):
        self.device_range_label = DeviceRangeLabel(window, start_row)
        self.device_range_entry_min = DeviceRangeEntryMin(window, module, start_row+1)
        self.device_range_entry_max = DeviceRangeEntryMax(window, module, start_row+1)


class DeviceRangeLabel(TextLabel):
    def __init__(self, window, row):
        super().__init__(window, text="Device Range [min - max]", width=25)
        self.grid(row=row, column=0, columnspan=2, padx=10, sticky="n")


class DeviceRangeEntryMin(TextEntry):
    def __init__(self, window, module, row):
        super().__init__(window, module.device_range_min)
        self.grid(row=row, column=0, padx=10, sticky="nw")


class DeviceRangeEntryMax(TextEntry):
    def __init__(self, window, module, row):
        super().__init__(window, module.device_range_max)
        self.grid(row=row, column=1, padx=10, sticky="ne")
