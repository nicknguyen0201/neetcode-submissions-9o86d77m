from functools import cache
class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        @cache
        def dfs(l,r):
            if l>r:
                return 0
            alice_turn = True if (r-l+1)%2 ==0 else False # alice go on even turn

            left= piles[l] if alice_turn else 0 #bob turn
            right=piles[r] if alice_turn else 0
            return max(left+ dfs(l+1,r), right + dfs(l,r-1))
        n=len(piles)
        res=dfs(0,n-1)
        return True if  res > (sum(piles) - res) else False