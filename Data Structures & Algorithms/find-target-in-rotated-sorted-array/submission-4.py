class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        target=3
        [4, 5, 6, 1, 2, 3]
         l     m  l     r

        find

        """
        #pass 1 find peak
        l,r=0,len(nums)-1
        while l<r:
            #if 
            mid=(l+r)//2
            if nums[mid]<nums[r]:
                r=mid
            else:
                l=mid+1
        piviot=l

        #pass 2
        l,r=0,len(nums)-1
        if nums[r]>=target>=nums[piviot]:
            l=piviot
        else:
            r=piviot-1
        
        while l<=r:
            mid=(l+r)//2
            if target==nums[mid]:
                return mid
            elif target<nums[mid]:
                r=mid-1
            else:
                l=mid+1
        return -1


