my_array1 = [70, 30, 10, 50, 100, 2] #test case 1
my_array2 = [5,2,3,1] #test case 2
my_array3 = [45, 10, 63, 40, 50, 80] #test case 3

'''
Time complexity: O(n^2)
Space complexity: O(1)
'''
def bubble_sort(arr):
    arr_length = len(arr)
    for i in range(arr_length):
        for j in range(i+1, arr_length):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr          


print(bubble_sort(my_array1))
print(bubble_sort(my_array2))
print(bubble_sort(my_array3))

            