import os

def test_ft2m30(capfd):
    os.system('echo "30" | python ft2m.py')
    out, err = capfd.readouterr()
    out = out.strip()
    assert out == "9.14"

def test_ft2m19_68504(capfd):
    os.system('echo "19.68504" | python ft2m.py')
    out, err = capfd.readouterr()
    out = out.strip()
    assert out == "6.00"