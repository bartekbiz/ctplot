from controls.base.LabelValue import LabelValue


class PlotStatistics:
    def __init__(self, window):
        row = 1
        self.max_value = MaxValue(window, row)
        self.min_value = MinValue(window, row+1)
        self.max_velocity = MaxVelocity(window, row+2)
        self.min_velocity = MinVelocity(window, row+3)
        self.max_acceleration = MaxAcceleration(window, row+4)
        self.min_acceleration = MinAcceleration(window, row+5)

class MaxValue(LabelValue):
    def __init__(self, window, row):
        super().__init__(window, text="Max Value", row=row, column=0)

class MinValue(LabelValue):
    def __init__(self, window, row):
        super().__init__(window, text="Min Value", row=row, column=0)

class MaxVelocity(LabelValue):
    def __init__(self, window, row):
        super().__init__(window, text="Max Velocity", row=row, column=0)

class MinVelocity(LabelValue):
    def __init__(self, window, row):
        super().__init__(window, text="Min Velocity", row=row, column=0)

class MaxAcceleration(LabelValue):
    def __init__(self, window, row):
        super().__init__(window, text="Max Acceleration", row=row, column=0)

class MinAcceleration(LabelValue):
    def __init__(self, window, row):
        super().__init__(window, text="Min Acceleration", row=row, column=0)