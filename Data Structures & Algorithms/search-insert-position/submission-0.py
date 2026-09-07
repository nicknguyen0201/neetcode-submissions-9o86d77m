class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        [-1,0,2,4,6,8] t=10
          l     m     r        
        """
        l,r =0,len(nums)
        while l<r:
            mid=l+((r-l)//2)
            if nums[mid]>=target:
                r=mid
            else:
                l=mid+1
        return l
            
