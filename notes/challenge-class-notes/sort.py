def merge(a,b):
    '''Takes in two sorted arrays;
    merges them into one sorted array'''
    '''if len(a) < 1:
        return b
    if len(b) < 1:
        return a'''
    
    res = []
    while len(a) > 0 and len(b) > 0:
        if a[0] < b[0]:
            res.append(a[0])
            a = a[1:]
        else:
            res.append(b[0])
            b = b[1:]

    while len(b) > 0:
        res.append(b[0])
        b = b[1:]

    while len(a) > 0:
        res.append(a[0])
        a = a[1:]

    return res


def mergesort(unsorted):
    if len(unsorted) == 0:
        return []
    if len(unsorted) == 1:
        return unsorted
    
    midpoint = len(arr)//2
    
    left = mergesort(unsorted[:midpoint])
    right = mergesort(unsorted[midpoint:])
    
    #print(merge(left,right))
    return merge(left,right)