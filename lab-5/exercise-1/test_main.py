from main import printGreeting

def test_1(capfd):
    printGreeting("Giovanni", 25, "play golf")
    out,err = capfd.readouterr()
    out = out.strip()
    assert out == "Hello, my name is Giovanni, I am 25 years old, and I like to play golf."

def test_2(capfd):
    printGreeting("Angelo", 35, "drive my Tesla")
    out,err = capfd.readouterr()
    out = out.strip()
    assert out == "Hello, my name is Angelo, I am 35 years old, and I like to drive my Tesla."

def test_3(capfd):
    printGreeting("Keke", 7, "play the drums")
    out,err = capfd.readouterr()
    out = out.strip()
    assert out == "Hello, my name is Keke, I am 7 years old, and I like to play the drums."