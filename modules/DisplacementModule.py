
from controls.MinMaxFields import XMinMaxFields, YMinMaxFields
from modules.BaseModule import BaseModule
from enums.ModuleEnum import ModuleEnum

class DisplacementModule(BaseModule):
    def __init__(self, app):
        super().__init__(app)
        # ranges
        self.x_minmax_fields_1 = XMinMaxFields(self, row=4, text='x(t)', min_value = x_min, max_value= x_max) # how to pass x_min and x_max
        self.y_minmax_fields_1 = YMinMaxFields(self, row=6, text='x(t)')
        self.x_minmax_fields_2 = XMinMaxFields(self, row=8, text='v(t)', min_value = x_min_2, max_value= x_max_2) # how to pass x_min_2
        self.y_minmax_fields_2 = YMinMaxFields(self, row=10, text='v(t)')
        self.x_minmax_fields_3 = XMinMaxFields(self, row=12, text='a(t)', min_value = x_min_3, max_value= x_max_3)# how to pass x_min_3
        self.y_minmax_fields_3 = YMinMaxFields(self, row=14, text='a(t)')

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
