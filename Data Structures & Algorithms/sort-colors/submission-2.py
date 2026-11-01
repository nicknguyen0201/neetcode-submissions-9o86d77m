from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        [0,1,1,2,2]
           l   mr
        """
        left, mid, right = 0, 0, len(nums)-1
        while mid <= right:
            if nums[mid]== 0:
                nums[mid], nums[left] = nums[left], nums[mid]
                left += 1
                mid += 1
            elif nums[mid]==1:
                mid += 1
            else:
                nums[mid],nums[right]=nums[right], nums[mid]
                right -= 1
        
            
