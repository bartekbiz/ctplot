import controls.MinMaxFields
import controls.SpanField
import controls.ApplyButton

from plots.AnimatedPlot import AnimatedPlot


class BaseModule:
    def __init__(self, app):
        self.app = app

        # Plot related
        self.data = {"x": [], "y": []}
        self.plot = AnimatedPlot(app, self.data)

        # Apply button
        self.apply_button = None
        self.create_apply_button()

        # Input fields
        self.create_x_minmax_field()
        self.create_y_minmax_field()

        self.create_custom_span()

    def get_module_name(self):
        raise NotImplementedError()

    def create_x_minmax_field(self):
        controls.MinMaxFields.create_x_minmax_field(self)

    def create_y_minmax_field(self):
        controls.MinMaxFields.create_y_minmax_field(self)

    def create_apply_button(self):
        controls.ApplyButton.create_apply_button(self)

    def apply(self, *event):
        self.plot.create_plot()

    def create_custom_span(self):
        controls.SpanField.create_custom_span(self)
