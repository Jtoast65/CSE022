from main import addKeysToDictionary

def test_1():
    assert addKeysToDictionary({"Make": "Honda", "Model": "Accord", "Year": 2022, "Color": "Pearl White", "Price": 33660, "Horsepower": 252}, "MPG", "22 city / 32 highway") == {"Make": "Honda", "Model": "Accord", "Year": 2022, "Color": "Pearl White", "Price": 33660, "Horsepower": 252, "MPG": "22 city / 32 highway"}

def test_2():
    assert addKeysToDictionary({"Make": "Honda", "Model": "Accord", "Year": 2022, "Color": "Pearl White", "Price": 33660, "Horsepower": 252}, "Engine", "2.0 L 4-cylinder") == {"Make": "Honda", "Model": "Accord", "Year": 2022, "Color": "Pearl White", "Price": 33660, "Horsepower": 252, "Engine": "2.0 L 4-cylinder"}

def test_3():
    assert addKeysToDictionary({}, "Make", "Honda") == {"Make": "Honda"}