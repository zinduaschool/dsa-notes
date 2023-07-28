from houserobber import linerob

def circlerob(lst):
    if len(lst) == 0:
        return None
    if len(lst) == 1:
        return lst[0]
    return max(linerob(lst[:len(lst)-1]),linerob(lst[1:]))


if __name__ == '__main__':
    print(circlerob([2,1,2]))