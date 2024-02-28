import os

def test_f2c75(capfd):
    os.system('echo "75" | python f2c.py')
    out, err = capfd.readouterr()
    out = out.strip()
    assert out == "23.89"

def test_f2c73_4(capfd):
    os.system('echo "73.4" | python f2c.py')
    out, err = capfd.readouterr()
    out = out.strip()
    assert out == "23.00"