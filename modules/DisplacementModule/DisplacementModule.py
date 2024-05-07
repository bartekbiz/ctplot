from enums.ModuleEnum import ModuleEnum
from modules.BaseModule import BaseModule


class DisplacementModule(BaseModule):
    def __init__(self, app):
        super().__init__(
            app,
            plot_values={"x": "m", "v": "m/s", "a": "m/s^2"}
        )

    def get_name(self):
        return ModuleEnum.displacement

    def destroy(self, *event):
        super().destroy(*event)
