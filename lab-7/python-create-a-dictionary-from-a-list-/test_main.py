from main import createDictionaryFromLists

def test_1():
    assert createDictionaryFromLists(["Make", "Model", "Year", "Color", "Price", "Horsepower"], ["Honda", "Accord", 2022, "Pearl White", 33660, 252]) == {"Make": "Honda", "Model": "Accord", "Year": 2022, "Color": "Pearl White", "Price": 33660, "Horsepower": 252}

def test_2():
    assert createDictionaryFromLists(["Make", "Model", "Year", "Color", "Price", "Horsepower"], ["Toyota", "Camry", 2022, "Pearl White", 31145, 206]) == {"Make": "Toyota", "Model": "Camry", "Year": 2022, "Color": "Pearl White", "Price": 31145, "Horsepower": 206}