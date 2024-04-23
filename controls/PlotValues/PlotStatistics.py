from controls.base.LabelValue import LabelValue


class PlotStatistics:
    def __init__(self, module):
        row = 1
        self.max_value = MaxValue(module, row)
        self.min_value = MinValue(module, row+1)
        self.max_velocity = MaxVelocity(module, row+2)
        self.min_velocity = MinVelocity(module, row+3)
        self.max_acceleration = MaxAcceleration(module, row+4)
        self.min_acceleration = MinAcceleration(module, row+5)

class MaxValue(LabelValue):
    def __init__(self, module, row):
        super().__init__(module=module, text="Max Value", row=row, column=6)

class MinValue(LabelValue):
    def __init__(self, module, row):
        super().__init__(module=module, text="Min Value", row=row, column=6)

class MaxVelocity(LabelValue):
    def __init__(self, module, row):
        super().__init__(module=module, text="Max Velocity", row=row, column=6)

class MinVelocity(LabelValue):
    def __init__(self, module, row):
        super().__init__(module=module, text="Min Velocity", row=row, column=6)

class MaxAcceleration(LabelValue):
    def __init__(self, module, row):
        super().__init__(module=module, text="Max Acceleration", row=row, column=6)

class MinAcceleration(LabelValue):
    def __init__(self, module, row):
        super().__init__(module=module, text="Min Acceleration", row=row, column=6)