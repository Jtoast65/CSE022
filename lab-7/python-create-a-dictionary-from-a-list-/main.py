def createDictionaryFromLists(keys, values):
    car = {}
    for i in range(len(keys)):
        car[keys[i]] = values[i]
    return car
       
c = createDictionaryFromLists(["Make", "Color"], ["Cayenne", "Brown"])
print(c)
