class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """

        1 2 3 1 2
        3 2 1 2 1
        """
        dp=[1]*len(nums)
        
        for i in range(len(nums)-1,-1,-1):
            num=nums[i]
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    dp[i]=max(dp[j]+1,dp[i])
        return max(dp)