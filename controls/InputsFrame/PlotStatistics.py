from controls.base.LabelValue import LabelValue


class PlotStatistics:
    def __init__(self, window, module, start_row):
        self.max_value = MaxValue(window, start_row, module.plot_names[0])
        self.min_value = MinValue(window, start_row+1, module.plot_names[0])
        self.max_velocity = MaxVelocity(window, start_row+2, module.plot_names[1])
        self.min_velocity = MinVelocity(window, start_row+3, module.plot_names[1])
        self.max_acceleration = MaxAcceleration(window, start_row+4, module.plot_names[2])
        self.min_acceleration = MinAcceleration(window, start_row+5, module.plot_names[2])


class MaxValue(LabelValue):
    def __init__(self, window, row, name):
        super().__init__(window, text=f"Max {name}", row=row, col=0)


class MinValue(LabelValue):
    def __init__(self, window, row, name):
        super().__init__(window, text=f"Min {name}", row=row, col=0)


class MaxVelocity(LabelValue):
    def __init__(self, window, row, name):
        super().__init__(window, text=f"Max {name}", row=row, col=0)


class MinVelocity(LabelValue):
    def __init__(self, window, row, name):
        super().__init__(window, text=f"Min {name}", row=row, col=0)


class MaxAcceleration(LabelValue):
    def __init__(self, window, row, name):
        super().__init__(window, text=f"Max {name}", row=row, col=0)


class MinAcceleration(LabelValue):
    def __init__(self, window, row, name):
        super().__init__(window, text=f"Min {name}", row=row, col=0)
