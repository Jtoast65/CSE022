def isListSorted(myList):
    x = 1
    while x < len(myList):
        if myList[x-1] > myList[x]:
            return False
        x += 1
    return True 


p = isListSorted([1,2,3])
print(p)