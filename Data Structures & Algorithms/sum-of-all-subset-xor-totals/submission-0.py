class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res=0
        def dfs(start,sum):
            nonlocal res
            if start==len(nums):
                res+=sum
                return
            dfs(start+1,sum^(nums[start]))
            dfs(start+1,sum)
        dfs(0,0)
        return res

