cache = dict() #(w,maxW) | maxP
def knapsack(maxW,w,p):
    if len(w) == 0:
        return 0
    if len(w) == 1:
        if w[0] <= maxW:
            return p[0]
        return 0
    if (tuple(w),maxW) in cache.keys():
        return cache[(tuple(w),maxW)]
    if w[-1] <= maxW:
        a = p[-1] + knapsack(maxW-w[-1],w[:-1],p[:-1])
        b = knapsack(maxW,w[:-1],p[:-1])
        cache[(tuple(w),maxW)] = max(a,b)
        return cache[(tuple(w),maxW)]
    cache[(tuple(w),maxW)] = knapsack(maxW,w[:-1],p[:-1])
    return cache[(tuple(w),maxW)]


maxW = 8
w = [3,5,7]
p = [4,7,10]
print(knapsack(maxW,w,p))