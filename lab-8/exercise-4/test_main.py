from main import nextBirthdate

def test_1():
    result = nextBirthdate("birthdates.csv", "01/01/2022")
    assert result == "Draven Brock"

def test_2():
    result = nextBirthdate("birthdates.csv", "04/07/2022")
    assert result == "Shannon Brewer"

def test_3():
    result = nextBirthdate("birthdates.csv", "11/05/2022")
    assert result == "Ariella Wood"

def test_4():
    result = nextBirthdate("birthdates.csv", "09/02/2022")
    assert result == "Easton Mclean"

def test_5():
    result = nextBirthdate("birthdates.csv", "12/25/2022")
    assert result == "Draven Brock"