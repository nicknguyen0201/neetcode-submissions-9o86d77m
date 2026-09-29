class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total=sum(stones)
        target=total//2
        dp=[[0]*(target+1) for _ in range(len(stones)+1)]
        
        for i in range(1, len(stones)+1):
            for t in range(target+1):
                if t>=stones[i-1]:
                    dp[i][t]=max(dp[i-1][t],
                                stones[i-1] + dp[i-1][t-stones[i-1]] )
                else:
                    dp[i][t]=dp[i-1][t]
        return total-2*dp[len(stones)][target]