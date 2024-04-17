import pytest
import tkinter as tk
from app_ui.App import App

@pytest.fixture
def app():
    app = App()
    yield app

@pytest.fixture
def app_window():
    app = App()
    pump_events(app)
    yield app

    if app:
        app.destroy()
        pump_events(app)

def pump_events(app):
    while app.dooneevent(tk._tkinter.ALL_EVENTS | tk._tkinter.DONT_WAIT):
        pass

def test_title(app):
    assert app.title() == "CTPlot"

def test_window_dimensions(app):
    assert app.w_width == 960
    assert app.w_height == 720

def test_click_enter(app_window):
    app_window.event_generate('<Return>') 
    pump_events(app_window)
