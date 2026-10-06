from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq=Counter(nums)
        colors=list(freq)
        j=0
        for color in [0,1,2]:
            for i in range(freq[color]):
                nums[j]=color
                j+=1
            
