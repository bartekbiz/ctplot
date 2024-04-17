from modules.BaseModule import BaseModule
from enums.ModuleEnum import ModuleEnum


class DeviationModule(BaseModule):
    def __init__(self, app):
        super().__init__(app)

    def get_module_name(self):
        return ModuleEnum.deviation
