from main import lowestAverageTemperature

def test_1():
    result = lowestAverageTemperature("weather.csv")
    assert result == "Friday"