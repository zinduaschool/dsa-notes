def merge(left_arr, right_arr):
    
    sorted_arr = []

    while len(left_arr) > 0 and len(right_arr):
        if left_arr[0] < right_arr[0]:
            sorted_arr.append(left_arr[0])
            left_arr = left_arr[1:]
        else:
            sorted_arr.append(right_arr[0])
            right_arr = right_arr[1:]

    while len(right_arr) > 0:
        sorted_arr.append(right_arr[0])
        right_arr = right_arr[1:]

    while len(left_arr) > 0:
        sorted_arr.append(left_arr[0])
        left_arr = left_arr[1:]

    return sorted_arr



def mergesort(arr):

    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr
    
    left_arr = mergesort(arr[:len(arr)//2])
    right_arr = mergesort(arr[len(arr)//2:])

    return merge(left_arr, right_arr)


print(mergesort([23,96,45,34,1,78,13,12]))
