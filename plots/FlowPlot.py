from plots.AnimatedPlot import AnimatedPlot
class FlowPlot(AnimatedPlot):
    def __init__(self, window, app, data, plot_names, plot_units, plot_x_name):
        super().__init__(window, app, data, plot_names, plot_units, plot_x_name)

    def update_ax2_ax3_data(self):
        v_len = len(self.velocity_y)
        v_custom_range_min = v_len - 1 if v_len != 0 else 0

        a_len = len(self.acceleration_y)
        a_custom_range_min = a_len - 1 if a_len != 0 else 0

        v_x = self.animated_x
        v_y = [y * 50 for y in self.animated_y]
        a_x, a_y = self.plot_calculations.calc_linear_regression(v_x, v_y, self.span)

        self.ax2.plot(
            v_x[v_custom_range_min:],
            v_y[v_custom_range_min:],
            self.color
        )

        self.ax3.plot(
            a_x[a_custom_range_min:],
            a_y[a_custom_range_min:],
            self.color
        )
        self.velocity_y.extend(v_y[v_len:])
        self.acceleration_y.extend(a_y[a_len:])