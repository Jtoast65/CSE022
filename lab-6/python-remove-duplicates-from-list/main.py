def removeDuplicatesFromList(myList):
    return [*set(myList)]

p = removeDuplicatesFromList([1,2,2,3])
print(p)