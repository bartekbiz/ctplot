from enum import Enum


class ModuleEnum(Enum):
    displacement = "Displacement"
    flow = "Flow value"

    @staticmethod
    def parse_string(string: str):
        return ModuleEnum[string.lower().split(" ")[0]]
