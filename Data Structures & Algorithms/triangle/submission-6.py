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
        def dfs(level,i,sum):#2,0,5
            if level==tree_len:
                return sum
            new_sum=sum+triangle[level][i]#3
            res=dfs(level+1,i,new_sum)#dfs(4,0,15)
            res=min(res,dfs(level+1,i+1,new_sum))#dfs(1,1,2)
            return res
        return dfs(0,0,0)
