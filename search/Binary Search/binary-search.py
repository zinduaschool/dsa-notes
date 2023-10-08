'''
    Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 
'''
class Solution:

    #Optimal Soln  O(logn)
    def binarySearch(self, nums, target):

        left = 0 
        right = len(nums)-1

        while left <= right:
            midNum = round(( left + right ) // 2)

            if nums[midNum] == target:
                return midNum
            elif target < nums[midNum]:
                right = midNum -1
            else:
                left = midNum +1
        return -1

s = Solution()
print(s.binarySearch([-1,0,3,5,9,12], 9))   #4
print(s.binarySearch([-1,0,3,5,9,12], 2))   #-1