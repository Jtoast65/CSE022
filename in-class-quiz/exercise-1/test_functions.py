from functions import findPair


def test_findPair():
    amounts = [5,7,4,8,9,3,1,6,8,10,4]
    result = findPair(amounts, 19)

    assert result == [9,4] or result == [4,9]

    amounts = [4,8,9,3,1,6,8,10,4]
    result = findPair(amounts, 19)
    
    assert result == [7,2] or result == [2,7]

    amounts = [9,3,1,6,8,10,4]
    result = findPair(amounts, 19)
    
    assert result == [5,0] or result == [0,5]