from main import removeDuplicatesFromList

def test_1():
    assert removeDuplicatesFromList([1, 2, 3, 4, 5, 3]) == [1, 2, 3, 4, 5]

def test_2():
    assert removeDuplicatesFromList([1, 1, 2, 3, 3, 3, 4]) == [1, 2, 3, 4]

def test_3():
    assert removeDuplicatesFromList([1]) == [1]