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


def knapsack2(maxW,w,p):
    if len(w) == 0:
        return 0
    if len(w) == 1:
        if w[0] <= maxW:
            return p[0]
        return 0
    
    prev = [0] * (maxW+1)
    curr = [0] * (maxW+1)

    for i in range(len(w)):
        curr[0] = 0
        for j in range(1,maxW+1):
            if w[i] > j:
                curr[j] = prev[j]
            else:
                a = prev[j]
                b = p[i] + prev[j-w[i]]
                curr[j] = max(a,b)
        prev = curr

    return curr[-1]



maxW = 8
w = [1,3,5,7]
p = [2,4,7,10]
print(knapsack2(maxW,w,p))