class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        l ptr needed to keeptrack on the running minimum
        and greedily pick the next min day because it can only improve 
        profit so far

        """
        if len(prices)==1:
            return 0
        l,r=0,1
        profit=0
        for r in range(len(prices)):
            buy=prices[l]
            sell=prices[r]

            if sell>buy:
                profit=max(profit,sell-buy)
            else: #sell price <= buy, pick new sell as buy, update min running 
                l=r
        return profit
