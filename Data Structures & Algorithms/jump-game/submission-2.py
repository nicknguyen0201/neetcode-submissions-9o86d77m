class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        """
                0 1 2 3 4
        nums = [1,2,1,0,1]
        goal =4

        """
        goal=len(nums)-1
        for i in range( len(nums)-2,-1,-1):
            if nums[i]+i>=goal:
                goal=i
        return goal==0