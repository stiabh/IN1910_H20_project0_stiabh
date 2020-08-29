import calculator, math, pytest
tol = 1e-12

@pytest.mark.parametrize(
    "arg, expected_sum", [[(1, 2), 3], [(2, 2), 4], [(1, 1), 2]])

def test_add_exercise1(arg, expected_sum):
    assert calculator.add(arg[0], arg[1]) == expected_sum

@pytest.mark.parametrize(
    "arg2, expected_sum2", [[(0.1, 0.2), 0.3],
    [(0.2, 0.2), 0.4], [(0.1, 0.1), 0.2]])

def test_add_exercise2(arg2, expected_sum2):
    assert abs(calculator.add(arg2[0], arg2[1]) - expected_sum2) < tol

@pytest.mark.parametrize(
    "strings, string_sum",
    [[("Hello ", "World"), "Hello World"],
    [("foo", "bar"), "foobar"], [("abc", "def"), "abcdef"]])

def test_add_exercise3(strings, string_sum):
    assert calculator.add(strings[0], strings[1]) == string_sum

@pytest.mark.parametrize(
    "N", [5, 6, 7])

def test_factorial_exercise4(N):
    assert calculator.factorial(N) == math.factorial(N)

@pytest.mark.parametrize(
    "z", [math.pi/2, math.pi, math.pi/4])

def test_sin_exercise4(z):
    assert abs(calculator.sin(z, 20) - math.sin(z)) < tol

@pytest.mark.parametrize(
    "div, quot", [[(1, 2), 1/2], [(3, 4), 3/4], [(6, 5), 6/5]])

def test_divide_exercise4(div, quot):
    assert abs(calculator.divide(div[0], div[1]) - quot) < tol

@pytest.mark.parametrize(
    "w", [2, 3, 4])

def test_sqrt_exercise4(w):
    assert abs(calculator.sqrt(w) - math.sqrt(w)) < tol

@pytest.mark.parametrize(
    "s, s2", [[2, 4], [3, 9], [4, 16]])

def test_power2_exercise4(s, s2):
    assert calculator.power2(s) == s2

@pytest.mark.parametrize(
    "no, str", [[1, "x"], ["1", 2], [3, "y"]])

def test_add_raises_TypeError_for_string_arguments_exercise5(no, str):
    with pytest.raises(TypeError):
        calculator.add(no, str)

@pytest.mark.parametrize(
    "t", [2, 3, 4])

def test_divide_raises_ZeroDivisionError_when_div_by_zero_exercise5(t):
    with pytest.raises(ZeroDivisionError):
        calculator.divide(t, 0)