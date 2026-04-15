class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        """
        Plan:
        main tain l and r poitner
        when sum<target, exapnd
        when sum>= target, record, shrink
        review
        [2,1,5,1,5,3]
               l   r
        ws=9
        maxlen=3
        """
        if not nums:
            return 0
        min_len=float('infinity')
        l=0
        window_sum=0
        n=len(nums)
        for r in range(n):
            num = nums[r]
            if window_sum<target:
                window_sum+=num
            while window_sum >= target:
                min_len=min(min_len,r-l+1)
                window_sum-=nums[l]
                l+=1

        return 0 if min_len==float('infinity') else min_len

