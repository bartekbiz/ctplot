import pytest

from controls.MinMaxFields import XMinMaxFields
from plots.AnimatedPlot import AnimatedPlot
from app.App import App

@pytest.fixture
def app():
    app = App()
    yield app

@pytest.fixture
def plot(app):
    data = {"x": [], "y": []}
    plot = AnimatedPlot(app, data)
    yield plot

def test_max_value(plot):
    row = 2  # replace with your actual value
    text = "Test"  # replace with your actual value
    min_value = 1  # replace with your actual value
    max_value = 5  # replace with your actual value

    x_min_max_fields = XMinMaxFields(plot, row, text, min_value, max_value)

    plot.animated_y = [1, 2, 3, 5]
    assert plot.get_max_value() == 5

def test_min_value(plot):
    row = 2  # replace with your actual value
    text = "Test"  # replace with your actual value
    min_value = 1  # replace with your actual value
    max_value = 5  # replace with your actual value

    x_min_max_fields = XMinMaxFields(plot, row, text, min_value, max_value)
    plot.animated_y = [1, 2, 3, 5]
    assert plot.get_min_value() == 1


def test_max_velocity(plot):
    plot.velocity_y = [1, 2, 3, 5]
    assert plot.get_max_velocity() == 5 

def test_max_velocity_none(plot):
    plot.velocity_y = []
    assert plot.get_max_velocity() is None

def test_min_velocity(plot):
    plot.velocity_y = [1, 2, 3, 5]
    assert plot.get_min_velocity() == 1

def test_min_velocity_none(plot):
    plot.velocity_y = []
    assert plot.get_min_velocity() is None


def test_max_acceleration(plot):
    plot.acceleration_y = [1, 2, 3, 5]
    assert plot.get_max_acceleration() == 5 

def test_max_acceleration_none(plot):
    plot.acceleration_y = []
    assert plot.get_max_acceleration() is None

def test_min_acceleration(plot):
    plot.acceleration_y = [1, 2, 3, 5]
    assert plot.get_min_acceleration() == 1

def test_min_acceleration_none(plot):
    plot.acceleration_y = []
    assert plot.get_min_acceleration() is None
