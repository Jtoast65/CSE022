import os

def test_9_4(capfd):
    os.system("echo '9\n4' | python main.py")
    out,err = capfd.readouterr()
    out = out.strip()
    assert out == "* * * * * * * * *\n*               *\n*               *\n* * * * * * * * *"
