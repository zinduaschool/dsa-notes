## Summation of numbers
def sum_(n):
    '''Find the sum of '''
    if n == 1:
        return 1
    return sum_(n-1) + n


## Fibonacci numbers
def fibo(n):
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