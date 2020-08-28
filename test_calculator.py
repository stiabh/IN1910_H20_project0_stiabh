import calculator

def test_add_exercise1():
    assert calculator.add(1, 2) == 3

def test_add_exercise2():
    assert abs(calculator.add(0.1, 0.2) - 0.3) < 1e-12