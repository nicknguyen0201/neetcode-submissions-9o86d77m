class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp = [[float('infinity')]*(amount+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0]=0
        
        for i in range(1,n+1):
            num=coins[i-1]
            for j in range(1, amount+1):
                if j-num>=0:
                    dp[i][j] = min(dp[i-1][j],
                                    dp[i][j-num]+1
                                            )
                                    
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[n][amount] if dp[n][amount] != float('infinity') else -1