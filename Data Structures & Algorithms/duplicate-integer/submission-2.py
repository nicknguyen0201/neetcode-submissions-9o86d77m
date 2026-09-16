class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mp = defaultdict(int)
        for num in nums:
            if mp[num]>=1:
                return True
            mp[num]+=1
        return False
