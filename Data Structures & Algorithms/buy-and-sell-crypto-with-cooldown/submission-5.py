class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[0]*2 for _ in range(len(prices))]
        for i in range(len(prices)-1,-1,-1):
            for can_buy in [True, False]:
                if can_buy:
                    #pay for stock now + profit when you holding stock on next day
                    buy=0
                    if i+1<n:
                        buy=-prices[i]+dp[i+1][False]
                    else:
                        buy=-prices[i]
                    skip=0
                    if i+1<n:
                        #skip now + profit can buy next day
                        skip=dp[i+1][True]
                    #else: skip=0 because you don't have profit next day
                    dp[i][True]=max(buy,skip)
                else:
                    sell=0
                    if i+2<n:
                        #if you sell now, profit is sell price+ profit 2 days away when can buy again
                        sell=prices[i] +dp[i+2][True]
                    else: 
                        sell=prices[i]
                    skip=0
                    if i+1<n:
                        skip=dp[i+1][False]
                    #else: skip=0
                    dp[i][False]=max(sell,skip)
                        
        return dp[0][1]
