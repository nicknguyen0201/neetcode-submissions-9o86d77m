class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        1 2 2 3
        t=3

        """
        candidates.sort()
        def dfs(i,sum,path):
            if sum==target:
                res.append(path[:])
                return
            if sum>target:
                return
            if i==len(candidates):
                return
            path.append(candidates[i])#take
            dfs(i+1,sum+candidates[i],path)
            path.pop()
            while i+1<len(candidates) and candidates[i]==candidates[i+1]:
                i+=1
            dfs(i+1,sum,path)#skip
        res=[]
        dfs(0,0,[])
        return res

