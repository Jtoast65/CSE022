import os

def test_hello(capfd):
    os.system('python main.py')
    out, err = capfd.readouterr()
    out = out.strip()
    assert out == "Hello UC Merced"