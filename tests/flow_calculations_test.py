from app_ui.FlowCalculations import FlowCalculations
import pytest
from math import pi


@pytest.fixture
def data():
    data = {"x": [], "y": []}

    for i in range(100):
        data["x"].append(i)
        data["y"].append(i)

    yield data


@pytest.fixture
def flow_calculations(data):
    flow_calculations = FlowCalculations(data)
    yield flow_calculations


def test_get_value_from_volt(flow_calculations):
    assert flow_calculations.get_value_from_volt(5) == pytest.approx(250)
    assert flow_calculations.get_value_from_volt(0) == pytest.approx(0)
    assert flow_calculations.get_value_from_volt(10) == pytest.approx(500)


def test_calculate_average(flow_calculations):
    assert flow_calculations.calculate_average(
        flow_calculations.data["y"]
    ) == pytest.approx(49.5)


def test_calculate_cross_section_area(flow_calculations):
    assert flow_calculations.calculate_cross_section_area(2) == pytest.approx(pi)
    assert flow_calculations.calculate_cross_section_area(4) == pytest.approx(pi * 4)


def test_delete_close_to_zero_values(flow_calculations):
    data = {"x": [], "y": []}

    for i in range(4):
        data["x"].append(0)
        data["y"].append(0)

    for i in range(2):
        data["x"].append(123)
        data["y"].append(123)

    assert flow_calculations.delete_close_zero_values(data["y"], 1) == [123, 123]
