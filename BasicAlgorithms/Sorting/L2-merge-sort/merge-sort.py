my_array1 = [70, 30, 10, 50, 100, 2] #test case 1
my_array2 = [5,2,3,1] #test case 2
my_array3 = [45, 10, 63, 40, 50, 80] #test case 3


def merge_sort(nums):
    def split(arr):
        mid = len(arr) // 2
        left_array = arr[:mid]
        right_array = arr[mid:]
        return left_array, right_array


    def merge(left_array, right_array):
        arr = []
        j = 0
        i = 0

        while (i < len(left_array) and j < len(right_array)):
            if left_array[i] < right_array[j]:
                arr.append(left_array[i])
                i +=1
            else:
                arr.append(right_array[j])
                j +=1
            
        while i < len(left_array):
            arr.append(left_array[i])
            i +=1
            
        while j < len(right_array):
            arr.append(right_array[j])
            j +=1
        
        return arr

    if len(nums) <= 1:
        return nums
    
    left, right = split(nums)
    split_left = merge_sort(left)
    split_right = merge_sort(right)
    return merge(split_left, split_right)


print(merge_sort(my_array1))
print(merge_sort(my_array2))
print(merge_sort(my_array3))