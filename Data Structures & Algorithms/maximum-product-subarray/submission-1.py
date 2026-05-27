class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        dp[i]=max product when nums end at i index

        """
        if len( nums)==1:
            return nums[0]
        max_prod,min_prod=1,1
        res=max(nums)

        for num in nums:
            curr_max = num * max_prod
            #store the max at nums[i-1]
            max_prod=max(curr_max, min_prod*num, num)

            #store the min at nums[i-1]
            min_prod=min(curr_max, min_prod*num,num)
            res=max(res, max_prod)
        return res