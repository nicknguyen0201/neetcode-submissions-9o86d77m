class Solution:
    def maxTurbulenceSize(self, nums: List[int]) -> int:
        prev=''
        l,r=0,0
        res=1
        if len(nums)==1:
            return res
        while r<len(nums)-1:
            if nums[r]>nums[r+1] and prev!='>':
                prev='>'
                r+=1
                res=max(r-l+1,res)
            elif nums[r]<nums[r+1] and prev!='<':
                prev='<'
                r+=1
                res=max(r-l+1,res)
            else:
                if nums[r]==nums[r+1]:
                    r+=1
                    l=r
                    prev=''
                else:
                    l=r
                    r+=1
                    prev = '>'if r<len(nums) and nums[l]>nums[r] else '<'
                
        return res
        """
            [2,4,3,2,2,5,1,4]
                   l r
        res=2
        prev='>'

        """
