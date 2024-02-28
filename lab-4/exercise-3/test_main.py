import os

def test_10(capfd):
    os.system("echo '10' | python main.py")
    out,err = capfd.readouterr()
    out = out.strip()
    assert out == "2\n4\n6\n8\n10"
