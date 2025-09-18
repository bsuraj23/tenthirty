#62.What is mocking in Python testing?
from unittest.mock import Mock

# Pretend this is a 3rd-party API
class WeatherAPI:
    def get_temperature(self, city):
        pass

def get_weather_report(api, city):
    temp = api.get_temperature(city)
    return f"The temperature in {city} is {temp}°C"

def test_weather_report():
    fake_api = Mock()
    fake_api.get_temperature.return_value = 25

    result = get_weather_report(fake_api, "Delhi")
    assert result == "The temperature in Delhi is 25°C"
