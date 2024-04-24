from controls.base.Frame import Frame
from controls.ButtonsFrame.OpenCSVButton import OpenCSVButton
from controls.ButtonsFrame.CloseButton import CloseButton
from controls.base.Separator import Separator


class ButtonsFrame(Frame):
    def __init__(self, app, module):
        super().__init__(app.column_0_frame, row=1)

        self.open_csv_button = OpenCSVButton(self, module, row=0)
        self.close_button = CloseButton(self, module, row=1)
        Separator(self, row=3)
