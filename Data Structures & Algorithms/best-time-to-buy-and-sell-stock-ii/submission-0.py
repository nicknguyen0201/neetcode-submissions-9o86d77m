class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        can_buy,hold=0,0
        next_buy,next_hold=0,0
        for i in range(len(prices)-1,-1,-1):
            price=prices[i]
            next_buy=max(can_buy,hold-price)
            next_hold=max(hold,can_buy+price)

            can_buy=next_buy
            hold=next_hold
        return next_buy