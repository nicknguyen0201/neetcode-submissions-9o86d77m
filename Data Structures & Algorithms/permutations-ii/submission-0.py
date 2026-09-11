from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        [1,1,2]
        [1,2]
        """
        freq=Counter(nums)
        res=[]

        def dfs(perm):
            if len(perm)==len(nums):
                res.append(perm[:])
            for key,val in freq.items():
                if val>0:
                    perm.append(key)
                    freq[key]-=1
                    dfs(perm)
                    perm.pop()
                    freq[key]+=1        
        dfs([])
        return res