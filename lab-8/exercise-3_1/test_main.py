from main import updatePassword

f = open("credentials.csv", "w")
original = ['Netflix,jdoe@ucmerced.edu,807@Bk\n', 'Hulu,jdoe@ucmerced.edu,F!118l\n', 'Peacock,jdoe@ucmerced.edu,5&21zH\n', 'HBO Max,jdoe@ucmerced.edu,0P@88v\n', 'Disney Plus,jdoe@ucmerced.edu,&41e6I\n', 'Apple TV,jdoe@ucmerced.edu,626@Kl']
for line in original:
    f.write(line)
f.close()

def test_1():
    updatePassword("credentials.csv", "Netflix", "abc123")
    f = open("credentials.csv", "r")
    result = f.readlines()
    f.close()
    assert result == ['Netflix,jdoe@ucmerced.edu,abc123\n', 'Hulu,jdoe@ucmerced.edu,F!118l\n', 'Peacock,jdoe@ucmerced.edu,5&21zH\n', 'HBO Max,jdoe@ucmerced.edu,0P@88v\n', 'Disney Plus,jdoe@ucmerced.edu,&41e6I\n', 'Apple TV,jdoe@ucmerced.edu,626@Kl']

def test_2():
    updatePassword("credentials.csv", "Peacock", "def456")
    f = open("credentials.csv", "r")
    result = f.readlines()
    f.close()
    assert result == ['Netflix,jdoe@ucmerced.edu,abc123\n', 'Hulu,jdoe@ucmerced.edu,F!118l\n', 'Peacock,jdoe@ucmerced.edu,def456\n', 'HBO Max,jdoe@ucmerced.edu,0P@88v\n', 'Disney Plus,jdoe@ucmerced.edu,&41e6I\n', 'Apple TV,jdoe@ucmerced.edu,626@Kl']

def test_3():
    updatePassword("credentials.csv", "Disney Plus", "ijk789")
    f = open("credentials.csv", "r")
    result = f.readlines()
    f.close()
    assert result == ['Netflix,jdoe@ucmerced.edu,abc123\n', 'Hulu,jdoe@ucmerced.edu,F!118l\n', 'Peacock,jdoe@ucmerced.edu,def456\n', 'HBO Max,jdoe@ucmerced.edu,0P@88v\n', 'Disney Plus,jdoe@ucmerced.edu,ijk789\n', 'Apple TV,jdoe@ucmerced.edu,626@Kl']

def test_4():
    updatePassword("credentials.csv", "Disney Plus", "&41e6I")
    f = open("credentials.csv", "r")
    result = f.readlines()
    f.close()
    assert result == ['Netflix,jdoe@ucmerced.edu,abc123\n', 'Hulu,jdoe@ucmerced.edu,F!118l\n', 'Peacock,jdoe@ucmerced.edu,def456\n', 'HBO Max,jdoe@ucmerced.edu,0P@88v\n', 'Disney Plus,jdoe@ucmerced.edu,&41e6I\n', 'Apple TV,jdoe@ucmerced.edu,626@Kl']

def test_5():
    updatePassword("credentials.csv", "Apple tv", "asdf1234")
    f = open("credentials.csv", "r")
    result = f.readlines()
    f.close()
    assert result == ['Netflix,jdoe@ucmerced.edu,abc123\n', 'Hulu,jdoe@ucmerced.edu,F!118l\n', 'Peacock,jdoe@ucmerced.edu,def456\n', 'HBO Max,jdoe@ucmerced.edu,0P@88v\n', 'Disney Plus,jdoe@ucmerced.edu,&41e6I\n', 'Apple TV,jdoe@ucmerced.edu,626@Kl']
    