class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp=defaultdict(int)
        dp[0]=1
        for num in nums:
            next_dp=defaultdict(int)
            for sum,cnt in dp.items():
                next_dp[sum+num]+=cnt
                next_dp[sum-num]+=cnt
            dp=next_dp
        return dp[target]