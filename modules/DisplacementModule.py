from controls.MinMaxFields import XMinMaxFields, YMinMaxFields
from modules.BaseModule import BaseModule
from enums.ModuleEnum import ModuleEnum


class DisplacementModule(BaseModule):
    def __init__(self, app):
        super().__init__(app)
        # ranges
        self.x_minmax_fields = XMinMaxFields(self, row=4)
        self.y_minmax_fields = YMinMaxFields(self, row=4)
        self.x_minmax_fields_2 = XMinMaxFields(self, row=5)
        self.y_minmax_fields_2 = YMinMaxFields(self, row=5)
        self.x_minmax_fields_3 = XMinMaxFields(self, row=6)
        self.y_minmax_fields_3 = YMinMaxFields(self, row=6)

    def get_name(self):
        return ModuleEnum.displacement

    def close_module(self, *event):
        super().close_module(*event)
        self.x_minmax_fields.destroy()
        self.y_minmax_fields.destroy()
        self.x_minmax_fields_2.destroy()
        self.y_minmax_fields_2.destroy()
        self.x_minmax_fields_3.destroy()
        self.y_minmax_fields_3.destroy()
