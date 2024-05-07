import pytest

from app.App import App


@pytest.fixture
def app():
    app = App()
    yield app


@pytest.fixture
def plot(app):
    data = {"x": [], "y": []}
    plot = app.current_module.plot
    yield plot


def test_max_value(plot):
    plot.animated_y = [1, 2, 3, 5]
    assert plot.get_max_value() == 5


def test_min_value(plot):
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
