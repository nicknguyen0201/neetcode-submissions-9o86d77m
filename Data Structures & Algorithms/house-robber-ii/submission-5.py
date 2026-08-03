class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums)
        def solve(nums):
            n = len(nums)
            dp=[0]*n
            dp[n-1] = nums[n-1]
            dp[n-2]=max(nums[n-2],nums[n-1])

            for i in range( n-3, -1,-1):
                dp[i]=max(dp[i+2]+nums[i], dp[i+1])
            return dp[0]
        
        return max(solve(nums[:-1]), solve(nums[1:]))
        """
        return max(12,15)
        [2,9,8,3,6]
        s=1
        end=5
        dp
        [ 15 14 6 6]
        """
