import os

def test_7(capfd):
    os.system("echo '7' | python main.py")
    out,err = capfd.readouterr()
    out = out.strip()
    assert out == "7 x 1 = 7\n7 x 2 = 14\n7 x 3 = 21\n7 x 4 = 28\n7 x 5 = 35\n7 x 6 = 42\n7 x 7 = 49\n7 x 8 = 56\n7 x 9 = 63\n7 x 10 = 70\n7 x 11 = 77\n7 x 12 = 84"
