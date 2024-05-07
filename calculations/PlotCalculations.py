import numpy as np
from sklearn.linear_model import LinearRegression


class PlotCalculations:
    @staticmethod
    def calc_linear_regression(x, y, span=30):
        result_x = []
        result_y = []

        for i in range(len(x) - span):
            xs = np.array(x[i:i + span]).reshape((-1, 1))
            ys = np.array(y[i:i + span])

            reg = LinearRegression(n_jobs=2).fit(xs, ys)

            result_x.append(x[i])

            result_y.append((reg.coef_ * x[i])[0])

        return result_x, result_y
