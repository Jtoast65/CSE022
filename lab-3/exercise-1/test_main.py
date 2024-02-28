import os

def test_17(capfd):
    os.system("echo '17' | python main.py")
    out,err = capfd.readouterr()
    out = out.strip()
    assert out == "The number is positive."

def test_0(capfd):
    os.system("echo '0' | python main.py")
    out,err = capfd.readouterr()
    out = out.strip()
    assert out == ""

def test_17n(capfd):
    os.system("echo '-17' | python main.py")
    out,err = capfd.readouterr()
    out = out.strip()
    assert out == ""