from modules.BaseModule import BaseModule
from enums.ModuleEnum import ModuleEnum


class DisplacementModule(BaseModule):
    def __init__(self, app):
        super().__init__(
            app,
            plot_names=["x", "v", "a"]
        )

    def get_name(self):
        return ModuleEnum.displacement

    def destroy(self, *event):
        super().destroy(*event)


