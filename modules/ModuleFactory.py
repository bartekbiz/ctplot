from enums.ModuleEnum import ModuleEnum

from modules.BaseModule import BaseModule
from modules.DisplacementModule import DisplacementModule
from modules.DeviationModule import DeviationModule
from modules.FlowModule import FlowModule
from modules.RotationModule import RotationModule


class ModuleFactory:
    @staticmethod
    def make_module(module: ModuleEnum, app) -> BaseModule:
        if module == ModuleEnum.displacement:
            return DisplacementModule(app)

        elif module == ModuleEnum.deviation:
            return DeviationModule(app)

        elif module == ModuleEnum.flow:
            return FlowModule(app)

        elif module == ModuleEnum.rotation:
            return RotationModule(app)

        else:
            raise Exception("Wrong arg passed to make_module method!")
