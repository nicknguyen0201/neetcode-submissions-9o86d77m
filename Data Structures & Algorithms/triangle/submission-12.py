from functools import cache
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        tree_len=len(triangle)
        
        dfs(level,i,sum):

            if level=tree_len:
                return res
            
            res=dfs()
            res=max(res,dfs())
        """
        n=len(triangle)
        dp=triangle[n-1].copy()
        for j in range(n-2,-1,-1):
            next_dp=triangle[j].copy()
            for i in range(len(dp)-1):
                next_dp[i]+=min(dp[i],dp[i+1])
            dp=next_dp
        return dp[0]