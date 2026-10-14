class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        1 3 5 7 6 4 2 1 0

        T T T T F F F F F 
              l,r    

        3,2,1
        l.  r         
        """
        l,r=0,len(nums)-1
      
        while l<r:
            m=l+(r-l)//2
            if nums[m]>nums[m+1]:
                r=m
              
            else:# nums[m]<=nums[m+1]:
                l=m+1
        return l
