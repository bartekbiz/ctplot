from enum import Enum


class ModuleEnum(Enum):
    displacement = "Displacement"
    deviation = "Deviation"
    flow = "Flow value"
    rotation = "Rotation speed"

    @staticmethod
    def parse_string(string: str):
        return ModuleEnum[string.lower().split(" ")[0]]
