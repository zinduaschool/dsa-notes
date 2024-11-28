## S(n) = s(n-1) + n
def sum_(n):
    if n < 0:
        return None
    if n == 0:
        return 0
    return n + sum_(n-1)


## f(n) = n * f(n-1)
def factorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    return n * factorial(n-1)


## f(n) = f(n-1) + f(n-2)
cache = dict() # n, value
def fibonacci(n):
    if n <= 0:
        return None
    if n == 1:
        return 1
    if n == 2:
        return 1
    
    if n in cache.keys():
        return cache[n]

    cache[n] = fibonacci(n-1) + fibonacci(n-2)
    return cache[n]


def fib(n):
    if n <= 0:
        return None
    if n == 1:
        return 1
    if n == 2:
        return 1
    a = 1
    b = 1
    for i in range(2,n):
        c = a + b
        a = b
        b = c
    return c


print(fib(1000000))