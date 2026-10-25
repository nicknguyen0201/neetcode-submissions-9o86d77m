
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
            2 pass bin search
            identify the peak
            search on the right subarr
        """
        def find_peak():
            """
            return peak index
             target=1       
            3,5,6,7,8,0,1,2]    
                        l r
            """
            l,r = 0, len(nums)-1
            while l < r:
                m = l + (r-l)//2
                if nums[m] > nums[r]:#still increasing side
                    l = m+1
                else:
                    r = m
            return l-1
        def find_target(l,r):
            while l<=r:
                m = l + (r-l) // 2
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m + 1
                else:
                    r = m - 1
            return -1
        peak=find_peak()
        if nums[-1] < target:
            return find_target(0,peak)
        else:# nums[-1]>target:
            return find_target(peak+1,len(nums)-1)
        


        

        
    