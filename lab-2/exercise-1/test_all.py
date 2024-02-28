import os

def test_c2f23(capfd):
    os.system('echo "23" | python c2f.py')
    out, err = capfd.readouterr()
    out = out.strip()
    assert out == "73.40"

def test_c2f23_89(capfd):
    os.system('echo "23.89" | python c2f.py')
    out, err = capfd.readouterr()
    out = out.strip()
    assert out == "75.00"