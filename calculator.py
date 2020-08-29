from math import pi

def add(x, y):
    return x + y

def factorial(N):
    if type(N) != int:
        raise ValueError("Not defined")
    else:
        if N < 0:
            raise ValueError("Not defined")
        elif N == 0:
            return 1
        else:
            prod = 1
            for n in range(1, N+1):
                prod *= n
    return prod

def sin(x, N):
    s = 0
    for n in range(N+1):
        s += ((-1)**n*x**(2*n+1))/factorial(2*n+1)
    return s