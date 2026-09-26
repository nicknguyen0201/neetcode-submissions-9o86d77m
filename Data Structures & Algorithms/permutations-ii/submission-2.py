class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        used=[False]*len(nums)
        nums.sort()
        def dfs(path):
            
            if len(path)==len(nums):
                res.append(path[:])
                return 
            
            for i in range(len(nums)):
                if not used[i]:
                    if i+1<len(nums) and nums[i]==nums[i+1] and not used[i+1]:
                        continue
                    path.append(nums[i])
                    used[i]=True
                    dfs(path)
                    used[i]=False
                    path.pop()
        dfs([])
        return res

