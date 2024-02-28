import os

def test_10(capfd):
    os.system("echo '1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n-1' | python main.py")
    out,err = capfd.readouterr()
    out = out.strip()
    assert out == "55"
