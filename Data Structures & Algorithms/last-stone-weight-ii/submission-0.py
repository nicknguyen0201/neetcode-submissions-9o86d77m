from functools import cache
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        """
        stone weight 1: we pick the largest stones and smash them and return 0 or the last stone w

        stone weight 2: we pick arbitrarily and 2 stone, smash them, finally return last stone with minimun w
        
        [4,4,1,7,10]
        way 1 (always pick smallest)

        [3,4,7,10]
        1,7,10
        1,3
        2

        way 2 (always pick biggest)
        [1,3,4,4]
        [1,3]
        [2]

        
        """
        sum_s=sum(stones)
        big_pile = (sum_s+1)//2
        @cache
        def dfs(i,total):
            if total>=big_pile or i>=len(stones):
                return abs(total - (sum_s-total))
            return min(dfs(i+1,total),dfs(i+1,total+stones[i]))
        return dfs(0,0)

