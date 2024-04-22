from modules.BaseModule import BaseModule
from enums.ModuleEnum import ModuleEnum


class DisplacementModule(BaseModule):
    def __init__(self, app):
        super().__init__(app)

    def get_name(self):
        return ModuleEnum.displacement
