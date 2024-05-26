class PlotCalculations:
    @staticmethod
    def calc_linear_regression(x, y, span):
        result_x = []
        result_dy_dx = []

        for i in range(len(x) - span):
            dx = x[i + span] - x[i]
            dy = y[i + span] - y[i]

            if dx != 0:
                dy_dx = dy / dx
                result_x.append(x[i])
                result_dy_dx.append(dy_dx)

        return result_x, result_dy_dx
