from controls.base.Frame import Frame
from controls.InputsFrame.DeviceRangeField import DeviceRangeField
from controls.InputsFrame.PlotStatistics import PlotStatistics
from controls.base.Separator import Separator


class InputsFrame(Frame):
    def __init__(self, app, module):
        super().__init__(app.column_0_frame, row=2, sticky="n")

        self.device_range_field = DeviceRangeField(self, module, start_row=0)
        Separator(self, row=20)
        self.plot_statistics = PlotStatistics(self, module, start_row=21)
        Separator(self, row=100)


