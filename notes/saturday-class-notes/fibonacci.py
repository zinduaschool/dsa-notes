'''
def fibo(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    
    if n in cache.keys():
        return cache[n]
    
    cache[n] = fibo(n-1) + fibo(n-2)
    return cache[n]


cache = dict()
print(fibo(10000))'''


def fibonacci(n):
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

    return b
        
        
print(fibonacci(10000))