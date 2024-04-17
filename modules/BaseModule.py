from plots.AnimatedPlot import AnimatedPlot


class BaseModule:
    def __init__(self, app):
        self.app = app

        self.plot = AnimatedPlot(app)

    def get_module_name(self):
        raise NotImplementedError()
