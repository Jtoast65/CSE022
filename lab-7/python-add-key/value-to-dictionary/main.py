def addKeysToDictionary(dictionary, keys, values):
    for i in range(len(keys)):
        dictionary[keys] = values
    return dictionary
x = addKeysToDictionary({"Make": "Cayenne", "Year": 2004}, "Horsepower", 252)
print(x)