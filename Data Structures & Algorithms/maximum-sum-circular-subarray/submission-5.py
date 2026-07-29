class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        [2,3,-4]
        max_s=0
        min_s=0
        rmax=2
        rmin=2
        total=0
        """
        max_subarr_sum=nums[0]
        min_subarr_sum=nums[0]
        running_max=0
        running_min=0
        total=0
        for num in nums:
            running_max=max(running_max+num,num)
            running_min=min(running_min+num,num)
            total+=num
            max_subarr_sum=max(running_max, max_subarr_sum)
            min_subarr_sum=min(running_min,min_subarr_sum)

        res=max(total-min_subarr_sum, max_subarr_sum)
        #if every elements are negative, we need to return global max
        #otherwise total-minsubarr =0 and suggests pick empty subarr
        return res if res>0 else max_subarr_sum