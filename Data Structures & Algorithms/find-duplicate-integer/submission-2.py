class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        node gonna be indices from 0 to n
        next ptr is the value inside nums[index]

        """
        #init pointers
        slow=0
        fast=0
        while True:
            fast = nums[nums[fast]]
            slow=nums[slow]
            if fast==slow:
                break
        slow2=0
        while slow!=slow2:
            slow=nums[slow]
            slow2=nums[slow2]

      
        return slow2
        
        