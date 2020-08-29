import calculator, math
tol = 1e-12

def test_add_exercise1():
    assert calculator.add(1, 2) == 3

def test_add_exercise2():
    assert abs(calculator.add(0.1, 0.2) - 0.3) < tol

def test_add_exercise3():
    assert calculator.add("Hello ", "World") == "Hello World"

def test_factorial_exercise4():
    assert calculator.factorial(6) == math.factorial(6)

def test_sin_exercise4():
    assert abs(calculator.sin(math.pi) - (-1)) < tol

def test_divide_exercise4():
    assert abs(calculator.divide(6, 5) - 6/5) < tol

def test_sqrt_exercise4():
    assert abs(calculator.sqrt(5) - math.sqrt(5)) < tol

def test_power2_exercise4():
    assert calculator.power2(9) == 81