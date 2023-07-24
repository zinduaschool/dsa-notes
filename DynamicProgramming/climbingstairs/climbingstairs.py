def climbingstairs(n,cache):
    '''Solution at n is taking 2 steps from 2 steps below or 1 step from 1 step below;
    ways to climb to n is thus equal to ways to climb at n-1 plus ways to climb at n-2'''
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n in cache.keys():
        return cache[n]
    cache[n] = climbingstairs(n-1, cache) + climbingstairs(n-2,cache)
    return cache[n]


def climbstairs(n):
    '''We'll implement bottom-up dynamic programming to solve the solution;
    this is the most optimal solution as they is no memory limit problem'''
    a = 1
    b = 2
    if n == 1:
        return a
    if n == 2:
        return b
    for i in range(2,n):
        c = a + b
        a = b
        b = c
    return b


if __name__ == '__main__':
    cache = dict()
    print(climbingstairs(12,cache), climbstairs(12))