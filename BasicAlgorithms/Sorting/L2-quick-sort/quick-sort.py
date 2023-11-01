my_array1 = [70, 30, 10, 50, 100, 2] #test case 1
my_array2 = [5,2,3,1] #test case 2
my_array3 = [45, 10, 63, 40, 50, 80] #test case 3

#With the pivot as the last element of the array
def partition(arr, low, high):
    pivot = arr[high]
    i = low -1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]

    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pivot_location = partition(arr, low, high)
        quick_sort(arr, low, pivot_location - 1)
        quick_sort(arr, pivot_location + 1, high)

    return arr

print(quick_sort(my_array1, 0, len(my_array1) - 1))
print(quick_sort(my_array2, 0, len(my_array2) - 1))
print(quick_sort(my_array3, 0, len(my_array3) - 1))