class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[[0]*(amount+1) for _ in range(len(coins)+1)]
        for i in range(len(coins)+1):
            dp[i][0]=1

        for i,coin in enumerate(coins):
            
            for amt in range(1,amount +1):
                if amt-coin >= 0:
                    dp[i+1][amt] = dp[i][amt]+dp[i+1][amt-coin]
                else:
                    dp[i+1][amt] = dp[i][amt]
        return dp[len(coins)][amount]