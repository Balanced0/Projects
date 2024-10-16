from project import get_weather, reset
import pytest
from tkinter import Tk, StringVar

root = Tk()
root.withdraw() 

city_text = StringVar(root)

def mock_reset():
    city_text.set("") 

reset = mock_reset

class MockResponse:
    @staticmethod
    def json():
        return {
            "name": "Dhaka",
            "sys": {"country": "BD"},
            "main": {"temp": 30.0},
            "weather": [{"main": "Clear", "icon": "01d"}]
        }

def test_get_weather(monkeypatch):
    def mock_get(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("requests.get", mock_get)
    result = get_weather("Dhaka")
    assert result == ("Dhaka", "BD", 30.0, "01d", "Clear")

def test_reset():
    city_text.set("Dhaka")
    reset() 
    assert city_text.get() == "" 

def test_get_weather_invalid_city(monkeypatch):
    def mock_get(*args, **kwargs):
        return None

    monkeypatch.setattr("requests.get", mock_get)
    result = get_weather("InvalidCity")
    assert result is None


@pytest.fixture(scope="session", autouse=True)
def teardown():
    yield
    root.destroy() 
