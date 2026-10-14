class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used=[False]*len(nums)
        res=[]
        def dfs(path):
            if len(path)==len(nums):
                res.append(path[:])
            for i in range(len(nums)):
                if not used[i]:
                    path.append(nums[i])
                    used[i]=True
                    dfs(path)
                    used[i]=False
                    path.pop()
        dfs([])
        return res
        