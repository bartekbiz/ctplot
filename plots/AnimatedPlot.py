from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from plots.MainPlot import MainPlot
from plots.PlotCalculations import PlotCalculations

class AnimatedPlot(MainPlot):
    def __init__(self, app):
        super().__init__(app)

        self.animated_x = []
        self.animated_y = []
        self.counter = 0

    def create_figure(self):
        # adding the subplot
        self.fig, (self.ax1, self.ax2, self.ax3) = plt.subplots(3, 1, constrained_layout=True)
        self.fig.set_figwidth(6.6)
        self.fig.set_figheight(6.6)

        self.set_single_plot_props(self.ax1, "Wykres x(t)", "x [m]", self.animated_x, self.animated_y)

        plot_calculations = PlotCalculations()

        v_x, v_y = plot_calculations.calc_linear_regression(self.animated_x, self.animated_y, 10)
        self.set_single_plot_props(self.ax2, "Wykres v(t)", "v [m/s]", v_x, v_y)

        a_x, a_y = plot_calculations.calc_linear_regression(v_x, v_y, 10)
        self.set_single_plot_props(self.ax3, "Wykres a(t)", "a [m/s*s]", a_x, a_y)

        self.animation = FuncAnimation(self.fig, self.update_frame, interval=5)

        # common axis labels
        self.fig.supxlabel("t [s]")

    def update_frame(self, frame):
        self.animated_x.append(self.app.data["x"][self.counter])
        self.animated_y.append(self.app.data["y"][self.counter])
        self.counter += 1
        self.ax1.plot(self.animated_x, self.animated_y)
        return self.ax1
        
    @staticmethod
    def set_single_plot_props(ax, title, y_label, x_data, y_data):
        ax.plot(x_data, y_data)
        ax.set_title(title)
        ax.set_ylabel(y_label)
        ax.grid()