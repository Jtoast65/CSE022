def isAFactor(a, b):
    if b % a == 0:
        return True
    return False

if isAFactor(6, 21) == False:
    print("False")
else:
    print("True")