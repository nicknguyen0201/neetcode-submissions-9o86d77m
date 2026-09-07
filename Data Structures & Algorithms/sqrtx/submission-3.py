class Solution:
    def mySqrt(self, x: int) -> int:
        """
            1 2 3 4 5 6 7 8 9 10
                lr m r                   

        """
        
        l=0
        r=x
        while l<r:
            mid=l+(r-l+1)//2
            #we want to find the LAST mid that ^2 <=x
            if mid**2<=x:
                l=mid
            else:
                r=mid-1
        return l