from main import findDifferencesBetweenLists

def test_1():
    result = findDifferencesBetweenLists([1, 2, 3, 4, 5], [3, 4, 5, 6, 7])
    result.sort()
    assert result == [1, 2, 6, 7]

def test_2():
    result = findDifferencesBetweenLists([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    result.sort()
    assert result == [6, 7, 8, 9, 10]

def test_3():
    result = findDifferencesBetweenLists([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])
    result.sort()
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]