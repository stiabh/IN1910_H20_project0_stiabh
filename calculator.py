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