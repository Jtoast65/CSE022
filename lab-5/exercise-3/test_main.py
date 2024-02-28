from main import perimeterOfRectangle

def test_1():
    assert perimeterOfRectangle(4, 16) == 40

def test_2():
    assert perimeterOfRectangle(3, 15) == 36

def test_3():
    assert perimeterOfRectangle(6, 21) == 54