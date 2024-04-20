from controls.FlowModule.DiameterField import DiameterField
from modules.BaseModule import BaseModule
from enums.ModuleEnum import ModuleEnum


class FlowModule(BaseModule):
    def __init__(self, app):
        super().__init__(app)
        self.diameter_field = DiameterField(self)

    def get_name(self):
        return ModuleEnum.flow
