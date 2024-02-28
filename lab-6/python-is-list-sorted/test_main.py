from main import isListSorted

def test_1():
    assert isListSorted([1, 2, 3]) == True

def test_2():
    assert isListSorted([1, 2, 3, 3, 2]) == False

def test_3():
    assert isListSorted([1, 2, 2, 3, 4, 5, 5]) == True