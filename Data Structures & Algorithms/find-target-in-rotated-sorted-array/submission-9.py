
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l<=r:
            m = l + (r-l) // 2
            if nums[m] == target:
                return m

            elif nums[l] <= nums[m]: #is left sub arr sorted

                if nums[l] <= target <= nums[m]: # is target inside the sorted range
                    r = m - 1
                else:
                    l = m + 1

            else: # then right sub array must be sorted
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1

        return -1
        


        

        
    