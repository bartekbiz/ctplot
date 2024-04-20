from controls.base.TextLabel import TextLabel
from controls.base.TextEntry import TextEntry


class DeviceRangeField:
    def __init__(self, module):
        self.device_range_label = DeviceRangeLabel(module)
        self.device_range_entry_min = DeviceRangeEntryMin(module)
        self.device_range_entry_max = DeviceRangeEntryMax(module)


class DeviceRangeLabel(TextLabel):
    def __init__(self, module):
        super().__init__(module.app, text="Device Range [min - max]", width=20)
        self.grid(row=10, column=0, padx=10, sticky="nw")


class DeviceRangeEntryMin(TextEntry):
    def __init__(self, module):
        super().__init__(module.app, module.device_range_min)
        self.grid(row=11, column=0, padx=10, sticky="nw")


class DeviceRangeEntryMax(TextEntry):
    def __init__(self, module):
        super().__init__(module.app, module.device_range_max)
        self.grid(row=11, column=1, padx=10, sticky="ne")
