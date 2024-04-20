from controls.MinMaxFields import XMinMaxFields, YMinMaxFields
from modules.BaseModule import BaseModule
from enums.ModuleEnum import ModuleEnum


class DisplacementModule(BaseModule):
    def __init__(self, app):
        super().__init__(app)
        # ranges
        self.x_minmax_fields_1 = XMinMaxFields(self, row=4, text='x(t)')
        self.y_minmax_fields_1 = YMinMaxFields(self, row=5, text='x(t)')
        self.x_minmax_fields_2 = XMinMaxFields(self, row=6, text='v(t)')
        self.y_minmax_fields_2 = YMinMaxFields(self, row=7, text='v(t)')
        self.x_minmax_fields_3 = XMinMaxFields(self, row=8, text='a(t)')
        self.y_minmax_fields_3 = YMinMaxFields(self, row=9, text='a(t)')

    def get_name(self):
        return ModuleEnum.displacement

    def close_module(self, *event):
        super().close_module(*event)
        self.x_minmax_fields_1.destroy()
        self.y_minmax_fields_1.destroy()
        self.x_minmax_fields_2.destroy()
        self.y_minmax_fields_2.destroy()
        self.x_minmax_fields_3.destroy()
        self.y_minmax_fields_3.destroy()
