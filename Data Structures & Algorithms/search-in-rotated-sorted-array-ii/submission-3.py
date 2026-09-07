class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """def binsearch(l,r):
            while l<=r:
                m=l+(r-l)//2
                if nums[m]==target:
                    return True
                elif nums[m]<target:
                    l=m+1
                else:
                    r=m-1
            return False"""
        
        l,r=0, len(nums)-1
        while l<=r:
            mid=l+(r-l)//2
            if nums[mid]==target:
                return True
            elif nums[mid]>nums[l]:
                #mid is in left portion 
                #check if target contains inside
                if nums[l]<=target<nums[mid]:
                    r=mid-1
                    #return binsearch(l,r)
                else:
                    l=mid+1
            elif nums[mid]<nums[l]:
                #mid is in the right portion
                #check if target is contained
                if nums[mid]<=target<= nums[r]:
                    l=mid
                    #return binsearch(l,r)
                else:
                    r=mid-1
            else:
                l+=1
        return False