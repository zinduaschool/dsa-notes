def linerob(lst):
    if len(lst) == 0:
        return None
    a = lst[0]
    if len(lst) == 1:
        return a
    b = max(lst[0], lst[1])
    if len(lst) == 2:
        return b
    for i in range(2,len(lst)):
        c = max(b,a+lst[i])
        a = b
        b = c
    return c

print(linerob([2,1,2,1,1,2]))