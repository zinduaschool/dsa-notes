def binarysearch(lst,a):
    start = 0
    finish = len(lst)-1
    
    while start<=finish:
        mid = (finish-start)//2
        if a == lst[mid]:
            return mid
        if a > lst[mid]:
            start = mid-1
        if a < lst[mid]:
            finish = mid+1
    return None