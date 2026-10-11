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
        tree_len=len(triangle)
        @cache
        def dfs(level,i):#2,0,5
            if level==tree_len:
                return 0
            res=triangle[level][i]+ dfs(level+1,i)
            res=min(res,triangle[level][i] + dfs(level+1,i+1))#dfs(1,1,2)
            return res
        return dfs(0,0)
