class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #curr_sum = the running sum
        #max_sub =. max of subarray sum ends at i
        max_sub,curr_sum = nums[0],0
        for num in nums:
            if curr_sum<0:
                curr_sum=0
            curr_sum+=num
            max_sub=max(max_sub, curr_sum)
        return max_sub