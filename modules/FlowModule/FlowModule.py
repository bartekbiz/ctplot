from tkinter import DoubleVar

from calculations.FlowCalculations import FlowCalculations
from controls.InputsFrame.FlowModule.CrossSectionField import CrossSectionField
from controls.InputsFrame.FlowModule.DiameterField import DiameterField
from controls.InputsFrame.FlowModule.FlowField import FlowField
from controls.InputsFrame.FlowModule.VAverageField import VAverageField
from enums.ModuleEnum import ModuleEnum
from modules.BaseModule import BaseModule


class FlowModule(BaseModule):
    def __init__(self, app):
        super().__init__(
            app,
            plot_values={"U": "V", "v*50": "mm", "a*50": "mm/s*s"}
        )

        self.flow_calculations = FlowCalculations(self.data)

        self.diameter_entry = DoubleVar()
        self.diameter_field = DiameterField(self.inputs_frame, self, row=10)
        
        self.v_average_entry = DoubleVar()
        self.v_average_field = VAverageField(self.inputs_frame, self, row=11)

        self.cross_section_field = CrossSectionField(self.inputs_frame, self, row=50)
        self.flow_field = FlowField(self.inputs_frame, self, row=51)
        # self.app.bind("t", self.update_flow_plot_stats)

    def update_cross_section(self, *event):
        self.cross_section_field.update_display(
            str(round(self.flow_calculations.calculate_cross_section_area(self.get_diameter()), 2)))

    def get_diameter(self) -> float:
        return float(self.diameter_field.diameter_entry.get())
    
    def get_v_average(self) -> float:
        return float(self.v_average_field.v_average_entry.get())
    
    def update_flow(self, *event):
        self.flow_field.update_display(
            str(round(self.flow_calculations.calculate_flow(self.get_v_average()), 2))
        )

    def get_name(self):
        return ModuleEnum.flow

    def destroy(self, *event):
        super().destroy(*event)

        self.diameter_field.destroy()
        self.cross_section_field.destroy()
        self.v_average_field.destroy()
        self.flow_field.destroy()

    # def update_flow_plot_stats(self, *event):
    #     self.flow_field.update_display(self.update_flow())
