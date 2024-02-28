from main import findElementsInCommon

def test_1():
    result = findElementsInCommon([1, 2, 3, 4, 5], [3, 4, 5, 6, 7])
    result.sort()
    assert result == [3, 4, 5]

def test_2():
    result = findElementsInCommon([1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    result.sort()
    assert result == [1, 2, 3, 4, 5]

def test_3():
    result = findElementsInCommon([1, 2, 3, 4, 5], [6, 7, 8, 9, 10])
    result.sort()
    assert result == []