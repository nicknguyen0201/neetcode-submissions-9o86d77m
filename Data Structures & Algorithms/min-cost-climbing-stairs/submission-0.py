from functools import cache
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        @cache
        def BT(i):
            if i>=len(cost):
                return 0

            res=0
            if i!=-1:
               res=cost[i]
            return res+ min( BT(i+1),BT(i+2) )
        return BT(-1)