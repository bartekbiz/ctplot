from controls.InputsFrame.FlowModule.DiameterField import DiameterField
from controls.InputsFrame.FlowModule.CrossSectionField import CrossSectionField
from controls.InputsFrame.FlowModule.VAverageField import VAverageField
from controls.InputsFrame.FlowModule.FlowField import FlowField

from calculations.FlowCalculations import FlowCalculations
from modules.BaseModule import BaseModule
from enums.ModuleEnum import ModuleEnum

from tkinter import DoubleVar


class FlowModule(BaseModule):
    def __init__(self, app):
        super().__init__(
            app,
            plot_values={"U": "V", "x": "m", "v": "m/s"}
        )

        self.flow_calculations = FlowCalculations(self.data)

        self.diameter_entry = DoubleVar()
        self.diameter_field = DiameterField(self.inputs_frame, self, row=10)

        self.cross_section_field = CrossSectionField(self.inputs_frame, self, row=50)
        self.v_average_field = VAverageField(self.inputs_frame, self, row=51)
        self.flow_field = FlowField(self.inputs_frame, self, row=52)
    
    def update_cross_section(self, *event):
        self.cross_section_field.update_display(str(round(self.flow_calculations.calculate_cross_section_area(self.get_diameter()), 2)))

    def get_diameter(self) -> float:
        return float(self.diameter_field.diameter_entry.get())
    
    # def update_v_average(self, *event):
    #     self.v_average_field.update_display(str(round(self.flow_calculations.v_average),2))

    # def update_flow(self, *event):
    #     self.flow_field.update_display(str(round(self.flow_calculations.flow, 2)))

    def get_name(self):
        return ModuleEnum.flow

    def destroy(self, *event):
        super().destroy(*event)

        self.diameter_field.destroy()
        self.cross_section_field.destroy()
        self.v_average_field.destroy()
        self.flow_field.destroy()
