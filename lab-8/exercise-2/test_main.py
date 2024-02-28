from main import queryContacts

def test_1():
    result = queryContacts("contacts.csv", 209)
    result.sort()
    assert result == ['Alfonso Reyes', 'Gilberto Valdez', 'Maggie Mack', 'Margarita Singleton', 'Miranda Padilla']

def test_2():
    result = queryContacts("contacts.csv", 559)
    result.sort()
    assert result == ['Angelo Brady', 'Barbara Lindsey', 'Bert Floyd', 'Erin Rose', 'Lena Obrien']

def test_3():
    result = queryContacts("contacts.csv", 716)
    result.sort()
    assert result == []