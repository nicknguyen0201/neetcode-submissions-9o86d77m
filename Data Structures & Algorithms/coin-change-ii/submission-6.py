class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        """
            0   1   2   3   4 amt
        1   1   1   1   1   1
        2   1   1   2   2   3   
        3   1   1   2   3   4
        
        coins
        """
        coins.sort()
        dp=[0]*(amount+1)
        dp[0]=1
        for coin in coins:
            for amt in range(1,amount+1):
                if amt-coin>=0:
                    dp[amt] = dp[amt-coin]+dp[amt]
        return dp[amount]