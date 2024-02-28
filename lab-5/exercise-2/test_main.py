from main import isAFactor

def test_1():
    assert isAFactor(4, 16) == True

def test_2():
    assert isAFactor(3, 15) == True

def test_3():
    assert isAFactor(6, 21) == False