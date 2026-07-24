class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
            0 1 2 3 4 5
            T F F F F F
        1   T
        2   T
        3   T
        4   T
        """
        total=sum(nums)
        if total%2!=0:
            return False
        target=total//2
        dp=[[False]*(target+1) for _ in range(len(nums)+1)]
        for i in range(len(nums)+1):
            dp[i][0]=True

        for r in range(1,len(nums)+1):
            for c in range(1,target+1):
                i=r-1
                if c - nums[i]>=0:
                    dp[r][c] = dp[r-1][c-nums[i]]
                dp[r][c] |= dp[r-1][c]
        return dp[len(nums)][target]