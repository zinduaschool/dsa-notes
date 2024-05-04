cache = dict() ## Key maxW, weights: ,max profit
def knapsack(maxW, profits, weights):
    if maxW== 0:
        return 0
    if len(weights) == 0:
        return 0
    if len(weights) == 1:
        return profits[0] if weights[0] <= maxW else 0
    if (maxW,tuple(weights)) in cache.keys():
        return cache[(maxW,tuple(weights))]
    if weights[-1] <= maxW:
        a = profits[-1] + knapsack(maxW-weights[-1],profits[:-1],weights[:-1])
        b = knapsack(maxW,profits[:-1],weights[:-1])
        cache[(maxW,tuple(weights))] = max(a,b)
        return cache[(maxW,tuple(weights))]
    cache[(maxW,tuple(weights))] = knapsack(maxW,profits[:-1],weights[:-1])
    return cache[(maxW,tuple(weights))]


def knapsack2(maxW,profits,weights):
    if maxW== 0:
        return 0
    if len(weights) == 0:
        return 0
    if len(weights) == 1:
        return profits[0] if weights[0] <= maxW else 0
    
    prev = [0] * (maxW+1)
    curr = [0] * (maxW+1)
    
    for i in range(len(weights)):
        curr[0] = 0
        for j in range(1,maxW+1):
            if weights[i] <= j and j-weights[i] >= 0:
                a = prev[j]
                b = profits[i] + prev[j-weights[i]]
                curr[j] = max(a,b)
            else:
                curr[j] = prev[j]
        prev = curr
    return curr[-1]

print(knapsack2(12,profits=[2,4,7,10],weights=[1,3,5,7]))