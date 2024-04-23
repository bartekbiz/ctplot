from math import pi, pow
from statistics import fmean, mean
from plots.PlotCalculations import PlotCalculations


class FlowCalculations:
    def __init__(self, data):
        self.data = data

        self.min_voltage = 0
        self.max_voltage = 10

        self.min_value = 0
        self.max_value = 500

        self.v_average = self.calculate_v_average(data['x'], data['y'])

        self.diameter = 40
        self.cross_section_area = self.calculate_cross_section_area(self.diameter)
        
        self.flow=self.v_average*self.cross_section_area

    def calculate_cross_section_area(self, diameter) -> float:
        return (pi * pow(diameter, 2)) / 4

    def get_value_from_volt(self, volts) -> float:
        return (self.max_value / self.max_voltage) * volts

    def calculate_v_average(self, data_x, data_y) -> float:
        _, velocity_y = PlotCalculations.calc_linear_regression(data_x, data_y)
        velocity_y = self.delete_close_zero_values(velocity_y, 1)
        return self.calculate_average(velocity_y)

    def delete_close_zero_values(self, data, treshold):
        result = []
        for i in range(len(data)):
            if abs(data[i]) > treshold:
                result.append(data[i])

        return result

    def calculate_average(self, data):
        return mean(data)

    def set_data(self, data):
        self.data = data
