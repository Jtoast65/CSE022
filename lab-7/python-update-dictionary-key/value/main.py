def updateDictionaryKey(dictionary, key, value):
    if key in dictionary:
        dictionary[key] = value
        return dictionary
    else:
        not_in = ("Key does not exist")
        return not_in

c = updateDictionaryKey({"Make": "Porsche", "Model": "Cayenne"}, "Color", "Cherry Red")
print(c)