import os

def test_12(capfd):
    os.system("echo '12' | python main.py")
    out,err = capfd.readouterr()
    out = out.strip()
    assert out == "The number is positive."

def test_0(capfd):
    os.system("echo '0' | python main.py")
    out,err = capfd.readouterr()
    out = out.strip()
    assert out == "The number is positive."

def test_12n(capfd):
    os.system("echo '-12' | python main.py")
    out,err = capfd.readouterr()
    out = out.strip()
    assert out == "The number is negative."