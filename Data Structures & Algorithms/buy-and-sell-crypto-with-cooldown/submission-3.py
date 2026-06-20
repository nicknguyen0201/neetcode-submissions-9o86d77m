from functools import cache
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def BT(i, can_buy):
            
            if i>=len(prices):
                return 0 
            
            hold = BT(i+1, can_buy)
            if can_buy:
                buy_profit = BT(i+1, False) - prices[i]
                return max(hold, buy_profit)
            else:
                sell_profit= BT(i+2, True)+prices[i]
                return max(hold, sell_profit)

        return BT(0,True)