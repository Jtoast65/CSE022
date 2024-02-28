from main import removeKeyFromDictionary

def test_1():
    assert removeKeyFromDictionary({"Make": "Honda", "Model": "Accord", "Year": 2022, "Color": "Pearl White", "Price": 33660, "Horsepower": 252}, "Color") == {"Make": "Honda", "Model": "Accord", "Year": 2022, "Price": 33660, "Horsepower": 252}

def test_2():
    assert removeKeyFromDictionary({"Make": "Honda", "Model": "Accord", "Year": 2022, "Color": "Pearl White", "Price": 33660, "Horsepower": 252}, "Horsepower") == {"Make": "Honda", "Model": "Accord", "Year": 2022, "Color": "Pearl White", "Price": 33660}

def test_3():
    assert removeKeyFromDictionary({"Make": "Honda", "Model": "Accord", "Year": 2022, "Color": "Pearl White", "Price": 33660, "Horsepower": 252}, "MPG") == "Key does not exist"