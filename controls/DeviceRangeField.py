from controls.base.TextLabel import TextLabel
from controls.base.TextEntry import TextEntry


class DeviceRangeField:
    def __init__(self, window, module):
        self.device_range_label = DeviceRangeLabel(window)
        self.device_range_entry_min = DeviceRangeEntryMin(window, module)
        self.device_range_entry_max = DeviceRangeEntryMax(window, module)


class DeviceRangeLabel(TextLabel):
    def __init__(self, window):
        super().__init__(window, text="Device Range [min - max]", width=30)
        self.grid(row=10, columnspan=2,column=0, padx=10, sticky="nw")


class DeviceRangeEntryMin(TextEntry):
    def __init__(self, window, module):
        super().__init__(window, module.device_range_min)
        self.grid(row=11, column=0, padx=10, sticky="nw")


class DeviceRangeEntryMax(TextEntry):
    def __init__(self, window, module):
        super().__init__(window, module.device_range_max)
        self.grid(row=11, column=1, padx=10, sticky="ne")
