from app_ui.FlowCalculations import FlowCalculations 
import pytest


@pytest.fixture
def data():
    data = {"x": [], "y": []}

    for i in range(100):
        data['x'].append(i)
        data['y'].append(i)

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
    assert flow_calculations.calculate_average(flow_calculations.data['y']) == pytest.approx(49.5)
