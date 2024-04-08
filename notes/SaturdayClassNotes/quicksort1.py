'''Average Time complexity: O(n log n)
Worst case scenario: O(n^2)'''


def quicksort(arr):
    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return arr
    else:
        pivot = arr[-1]
        left_arr = list()
        right_arr = list()

        for i in arr[:-1]:
            if i > pivot:
                right_arr.append(i)
            else:
                left_arr.append(i)
        
        return quicksort(left_arr) + [pivot] + quicksort(right_arr)

'''
Still working on the memory efficient quick sort methods below:
def partition(arr, left, right):
    #Takes in an array and its sub-indexes and returns the position for the next partition
    i = left
    j = right - 1
    pivot = arr[right]
    
    while i < j:
        while i < right and arr[i] < pivot:
            i += 1
        while j > left and arr[j] > pivot:
            j -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    if arr[i] > pivot:
        arr[i],arr[right]=arr[right],arr[i]
    return i


def quick_sort(arr, left, right):
    if left < right:
        pivot_pos = partition(arr, left, right)
        quick_sort(arr, pivot_pos, right)
        quick_sort(arr, left, pivot_pos)
    return arr
'''
arr = [23,96,45,34,1,78,13,12]
#print(quick_sort(arr, 0, len(arr)-1))
print(quicksort(arr))