from controls.base.Frame import Frame
from controls.PlotManipulationFrame.MinMaxFields import MinMaxFields
from controls.PlotManipulationFrame.SpanField import SpanField
from controls.PlotManipulationFrame.ResetButton import ResetButton
from controls.PlotManipulationFrame.ApplyButton import ApplyButton
from controls.base.Separator import Separator


class PlotManipulationFrame(Frame):
    def __init__(self, app, module):
        super().__init__(app.column_1_frame, row=0)

        self.minmax_fields = MinMaxFields(self, module, start_row=0)
        self.span_field = SpanField(self, module, row=16)
        Separator(self, row=17)
        self.reset_button = ResetButton(self, module, row=18, col=0)
        self.apply_button = ApplyButton(self, module, row=18, col=1)
