class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen=set()
        for i in range(k):
            if nums[i]not in seen:

                seen.add(nums[i])
            else:
                return True

        for i in range(k,len(nums)):
            if nums[i] in seen:
                return True
            seen.add(nums[i])
            seen.remove(nums[i-k])
        return False
