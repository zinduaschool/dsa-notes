## Find the nth term of a fibonacci sequence
def fibonacci(n):
    '''Top-down dynamic programming without memoization;
    Very simple to write but has n! complexity;
    this is felt when n is large'''
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)


def fibo(n, cache=dict()):
    '''Top-down dynamic programming with memoization (add cache);
    increases speed from n! to n as there are no repeated operations;
    memory limits make it impossible to compute when n is extremely large'''
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n in cache.keys():
        return cache[n]
    cache[n] = fibo(n-1,cache) + fibo(n-2,cache)
    return cache[n]


def fib(n):
    '''Bottom-up dynamic programming eliminates the memory limit problem when implementing memoization;
    memoization is still key as it improves the algorithm performance significantly
    this is the model to follow for all dynamic programming problems'''
    a = 0
    b = 1
    if n == 0:
        return a
    if n == 1:
        return b
    for i in range(2,n+1):
        c = a + b
        a = b
        b = c
    return b


    if __name__ == '__main__':
        print(fib(1000))