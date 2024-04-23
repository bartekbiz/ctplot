from controls.FlowModule.DiameterField import DiameterField
from controls.FlowModule.CrossSectionField import CrossSectionField
from controls.FlowModule.VAverageField import VAverageField
from controls.FlowModule.FlowField import FlowField
from calculations.FlowCalculations import FlowCalculations
from modules.BaseModule import BaseModule
from enums.ModuleEnum import ModuleEnum

from tkinter import DoubleVar


class FlowModule(BaseModule):
    def __init__(self, app):
        super().__init__(
            app,
            plot_1_y_title="U(t)",
            plot_2_y_title="X(t)",
            plot_3_y_title="v(t)"
        )

        self.diameter_entry = DoubleVar()
        self.diameter_field = DiameterField(self.user_inputs_frame, self, row=50)

        self.flow_calculations = FlowCalculations(self.data)

        self.cross_section_field = CrossSectionField(self.user_inputs_frame, self, row=51)
        self.v_average_field = VAverageField(self.user_inputs_frame, self, row=52)
        self.flow_field = FlowField(self.user_inputs_frame, self, row=53)
    
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
