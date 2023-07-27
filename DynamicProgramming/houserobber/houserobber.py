def houserobber(lst):
    if len(lst) == 1:
        return lst[0]
    if len(lst) == 2:
        if lst[0] > lst[1]:
            return lst[0]
        return lst[1]
    