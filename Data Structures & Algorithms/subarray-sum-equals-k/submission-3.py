class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum=defaultdict(int)
        prefix_sum[0] = 1 #base case
        running_sum=0
        result=0
        for num in nums:
            running_sum += num
            difference = running_sum-k
            result += prefix_sum[difference]
            prefix_sum[running_sum] += 1
        return result