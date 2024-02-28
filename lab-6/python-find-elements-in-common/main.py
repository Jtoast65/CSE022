def findElementsInCommon(listOne, listTwo):
    return list(set(listOne).intersection(listTwo))

p = findElementsInCommon([1,2,3,4], [4,5,6])
print(p)