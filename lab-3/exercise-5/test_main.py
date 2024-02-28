import os

def test_valid(capfd):
    os.system('printf "tim\nabc123" | python main.py')
    out, err = capfd.readouterr()
    out = out.strip()
    assert out == "Access Granted"

def test_valid_upcase(capfd):
    os.system('printf "Tim\nabc123" | python main.py')
    out, err = capfd.readouterr()
    out = out.strip()
    assert out == "Access Granted"

def test_valid_allcaps(capfd):
    os.system('printf "TIM\nabc123" | python main.py')
    out, err = capfd.readouterr()
    out = out.strip()
    assert out == "Access Granted"

def test_wrong_username(capfd):
    os.system('printf "steve\nabc123" | python main.py')
    out, err = capfd.readouterr()
    out = out.strip()
    assert out == "Incorrect Username/Password Combination"

def test_wrong_password(capfd):
    os.system('printf "tim\nabcd1234" | python main.py')
    out, err = capfd.readouterr()
    out = out.strip()
    assert out == "Incorrect Username/Password Combination"

def test_both_wrong(capfd):
    os.system('printf "steve\nabcd1234" | python main.py')
    out, err = capfd.readouterr()
    out = out.strip()
    assert out == "Incorrect Username/Password Combination"