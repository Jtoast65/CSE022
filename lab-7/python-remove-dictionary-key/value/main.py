def removeKeyFromDictionary(dictionary, keys):
    if keys in dictionary:
        dictionary.pop(keys)
        return dictionary
    else:
        not_in = ("Key does not exist")
        return not_in


c = removeKeyFromDictionary({"Model": "Porsche", "Year": 2022}, "Color")
print(c)