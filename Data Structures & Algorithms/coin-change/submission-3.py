class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
            1 , 5, 10

        [ 0  1  2  3  4  5. 6. 7. 8. 9. 10. 11. 12 ]
        [ 0  1. 1. 3  2  1. 3. 2. 4. 9. 2. 11.  3 ]
        """
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        for i in range(amount+1):
            for j,coin in enumerate(coins):
                if i-coin>=0:
                    dp[i]=min(dp[i-coin]+1,dp[i])
        return dp[amount] if dp[amount]!=float('inf') else -1
