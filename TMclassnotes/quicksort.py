def quicksort(arr):
    if len(arr) == 0:
        return []
    if len(arr) == 1:
        return arr

    left = list()
    right = list()
    pivot = arr[len(arr) - 1]

    for i in range(len(arr)-1):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quicksort(left) + [pivot] + quicksort(right)


print(quicksort([23,34,12,65,12, 18, 34, 9, 7, 56]))
