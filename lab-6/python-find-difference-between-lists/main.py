def findDifferencesBetweenLists(listOne, listTwo):
    return list(set(listOne).symmetric_difference(listTwo))

p = findDifferencesBetweenLists([1,2,3], [1,2])
print(p)
