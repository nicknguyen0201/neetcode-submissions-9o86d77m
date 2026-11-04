from functools import cache
class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        """
            I tried the bin search way, let's do top down and bot up dp

        """
        n=len(nums)
        @cache
        def BT(i,m):
            if i == n:
                if m == 0:
                    return 0
                return float('inf')
            if m == 0:
                return float('inf')
            
            curr_sum=0
            res=float('inf')
            for j in range(i,n-m+1):
                curr_sum += nums[j]
                res = min( res,max(curr_sum, BT(j+1, m-1)) )
            return res
        return BT(0,k)
