from controls.FlowModule.DiameterField import DiameterField
from controls.FlowModule.CrossSectionField import CrossSectionField
from app.FlowCalculations import FlowCalculations
from modules.BaseModule import BaseModule
from enums.ModuleEnum import ModuleEnum

from tkinter import DoubleVar


class FlowModule(BaseModule):
    def __init__(self, app):
        super().__init__(app)
        self.diameter_entry = DoubleVar()
        self.diameter_field = DiameterField(self)
        self.cross_section_field = CrossSectionField(self)

        self.flow_calculations = FlowCalculations(self.data)
    
    def update_cross_section(self, *event):
        self.cross_section_field.update_display(str(round(self.flow_calculations.calculate_cross_section_area(self.get_diameter()), 2)))

    def get_diameter(self) -> float:
        return float(self.diameter_field.diameter_entry.get())

    def get_name(self):
        return ModuleEnum.flow

    def close_module(self, *event):
        super().close_module(*event)

        self.diameter_field.destroy()
        self.cross_section_field.destroy()
