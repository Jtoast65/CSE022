import os

def test_7(capfd):
    os.system("echo '7' | python main.py")
    out,err = capfd.readouterr()
    out = out.strip()
    assert out == "The number is positive."

def test_0(capfd):
    os.system("echo '0' | python main.py")
    out,err = capfd.readouterr()
    out = out.strip()
    assert out == "The number is zero."

def test_7n(capfd):
    os.system("echo '-7' | python main.py")
    out,err = capfd.readouterr()
    out = out.strip()
    assert out == "The number is negative."