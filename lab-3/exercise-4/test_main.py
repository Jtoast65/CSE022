import os

def test_97(capfd):
    os.system("echo '97' | python main.py")
    out,err = capfd.readouterr()
    out = out.strip()
    assert out == "A"

def test_42(capfd):
    os.system("echo '42' | python main.py")
    out,err = capfd.readouterr()
    out = out.strip()
    assert out == "F"

def test_78(capfd):
    os.system("echo '78' | python main.py")
    out,err = capfd.readouterr()
    out = out.strip()
    assert out == "C"