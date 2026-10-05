from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        """
        1 [4, 2, 3 ,7 ] 1
           l        r 
        """
        n=len(nums)
        new_nums=[1]+nums+[1]
        @cache
        def dfs(l,r):
            if l>r:
                return 0
            res=0
            for i in range(l,r+1):
                coins=new_nums[l-1]*new_nums[i]*new_nums[r+1]
                coins +=dfs(l,i-1) + dfs(i+1,r)
                res=max(res,coins)
            return res
        return dfs(1,n)


