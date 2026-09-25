class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort(reverse=True)
        res=[]
        """
        [3,1,1]
        """
        def dfs(i,sum,path):
            if sum==target:
                res.append(path[:])
                return
            if sum>target or i==len(candidates):
                return
            path.append(candidates[i])
            dfs(i+1,sum+candidates[i],path)
            path.pop()#take
             
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1,sum,path)#skip all dup, also not taking 
            
        dfs(0,0,[])
        return res