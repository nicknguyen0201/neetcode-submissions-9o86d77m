class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        0                   6
        [1, 3, 3, 3, 3, 3, 4]
        l         m        r
        """
        def left_bisect(l,r):
            
            while l<r:
                m=l+(r-l)//2
                if nums[m]>=target:
                    r=m
                else:
                    l=m+1
            return l if nums[l]==target else -1
        def right_bisect(l,r):
            res=r
            while l<=r:
                m=l+(r-l)//2
                if nums[m]<=target:
                    l=m+1
                    res=m
                else:
                    r=m-1
            return res if nums[res]==target else-1
        if not nums:
            return [-1,-1]
        return [left_bisect(0,len(nums)-1),right_bisect(0,len(nums)-1)]