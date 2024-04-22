from enums.ModuleEnum import ModuleEnum

from modules.BaseModule import BaseModule
from modules.DisplacementModule.DisplacementModule import DisplacementModule
from modules.FlowModule.FlowModule import FlowModule


class ModuleFactory:
    @staticmethod
    def make_module(module: ModuleEnum, app) -> BaseModule:
        if module == ModuleEnum.displacement:
            return DisplacementModule(app)

        elif module == ModuleEnum.flow:
            return FlowModule(app)

        else:
            raise Exception("Wrong arg passed to make_module method!")
