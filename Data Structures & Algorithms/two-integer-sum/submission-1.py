class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        hashmap
        complement (=target-nums[i]) -> i
        5 (=7-2)        
        """
        mp=defaultdict(int)
        for i, num in enumerate(nums):
            if num not in mp:
                mp[target-num] = i
            else:
                return [mp[num],i]
        return [-1,-1]