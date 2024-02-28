import os

def test_m2ft6(capfd):
    os.system('echo "6" | python m2ft.py')
    out, err = capfd.readouterr()
    out = out.strip()
    assert out == "19.69"


def test_m2ft9_1439997074(capfd):
    os.system('echo "9.1439997074" | python m2ft.py')
    out, err = capfd.readouterr()
    out = out.strip()
    assert out == "30.00"