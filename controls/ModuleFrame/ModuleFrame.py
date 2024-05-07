from controls.ModuleFrame.MainLabel import MainLabel
from controls.ModuleFrame.ModuleDropdown import ModuleDropdown
from controls.base.Frame import Frame


class ModuleFrame(Frame):
    def __init__(self, app):
        super().__init__(app.column_0_frame, row=0)

        MainLabel(self)
        self.dropdown = ModuleDropdown(self, app)
