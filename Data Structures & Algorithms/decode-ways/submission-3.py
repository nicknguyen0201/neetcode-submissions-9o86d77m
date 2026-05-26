
from functools import cache
class Solution:
    def numDecodings(self, s: str) -> int:
        
        n=len(s)
        second_num={'0','1','2','3','4','5','6'}
        @cache
        def dfs(start):
            if start==n:
                return 1
            if s[start]=='0':
                return 0
            ways= dfs(start+1)
            if start+1<n and (s[start]=='1' or (s[start]=='2' and s[start+1] in second_num)):
                ways+=dfs(start+2)
        
            return ways
        return dfs(0)
        