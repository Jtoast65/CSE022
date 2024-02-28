def findPair(someList, target):
    required = {}
    for i in range(len(someList)):
        if target - someList[i] in required:
            return [required[target - someList[i]],i]
        else:
            required[someList[i]]=i
    return required