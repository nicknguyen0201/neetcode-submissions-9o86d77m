from functools import cache
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
        s = "c a a t", t = "c a t"
                   i               j
        """
        @cache
        def BT(i,j):
            if j>=len(t):
                return 1
            if i>=len(s):
                return 0
            ways=0
            if s[i]==t[j]:
                ways+= BT(i+1,j+1)
            ways+=BT(i+1,j)
            return ways
        return BT(0,0)
            