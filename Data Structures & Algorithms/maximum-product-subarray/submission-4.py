class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        right_prod=1
        left_prod=1
        res=nums[0]
        for i in range(len(nums)):
            right_prod=nums[i]*(right_prod or 1)
            left_prod=nums[len(nums)-1-i]*(left_prod or 1)
            res=max(res,right_prod,left_prod)
        return res