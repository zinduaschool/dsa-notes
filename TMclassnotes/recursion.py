## Summation of numbers
def sum_(n):
    '''Find the sum of numbers from 1 upto the nth number'''
    if n == 1:
        return 1
    return sum_(n-1) + n


## Fibonacci numbers
def fibo(n):
    '''Find the nth term of the fibonacci sequence'''
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fibo(n-1) + fibo(n-2)


print(sum_(10))
print(fibo(10))

## Merge sort and quick sort
'''Check code on these algorithms to understand where the recursion is applied'''
## Dynamic programming
'''Here we'll be doing recursion but on steroids (Optimise runtime and space complexity)'''