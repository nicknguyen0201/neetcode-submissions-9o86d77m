class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """
        Plan:
        dp[i] is different ways to get to i
        dp[target] is possible combinations to get to target
        """
        dp=defaultdict(int)
        dp[0]=1
        for t in range(1, target+1):
            for num in nums:
                dp[t]+=dp.get(t-num,0)
        return dp[target]
            
