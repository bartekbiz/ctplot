from modules.BaseModule import BaseModule
from enums.ModuleEnum import ModuleEnum


class DisplacementModule(BaseModule):
    def __init__(self, app):
        super().__init__(
            app,
            plot_1_y_title="x(t)",
            plot_2_y_title="v(t)",
            plot_3_y_title="a(t)"
        )

    def get_name(self):
        return ModuleEnum.displacement

    def destroy(self, *event):
        super().destroy(*event)


