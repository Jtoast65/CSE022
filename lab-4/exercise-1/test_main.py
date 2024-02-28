import os

def test_10(capfd):
    os.system("echo '1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n-1' | python main.py")
    out,err = capfd.readouterr()
    out = out.strip()
    assert out == "You entered: 1\nYou entered: 2\nYou entered: 3\nYou entered: 4\nYou entered: 5\nYou entered: 6\nYou entered: 7\nYou entered: 8\nYou entered: 9\nYou entered: 10\nDone"
