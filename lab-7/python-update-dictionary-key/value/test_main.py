from main import updateDictionaryKey

def test_1():
    assert updateDictionaryKey({"Make": "Honda", "Model": "Accord", "Year": 2022, "Color": "Pearl White", "Price": 33660, "Horsepower": 252}, "Color", "Cherry Red") == {"Make": "Honda", "Model": "Accord", "Year": 2022, "Color": "Cherry Red", "Price": 33660, "Horsepower": 252}

def test_2():
    assert updateDictionaryKey({"Make": "Honda", "Model": "Accord", "Year": 2022, "Color": "Pearl White", "Price": 33660, "Horsepower": 252}, "Price", 36999) == {"Make": "Honda", "Model": "Accord", "Year": 2022, "Color": "Pearl White", "Price": 36999, "Horsepower": 252}

def test_3():
    assert updateDictionaryKey({}, "Make", "Toyota") == "Key does not exist"