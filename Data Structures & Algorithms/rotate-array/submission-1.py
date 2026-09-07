class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        [1,2,3,4,5,6,7,8,9], k = 4
         l       r
        [9,8,7,6,5,4,3,2,1] reverse 1

        [6,7,8,9,5,4,3,2,1] 2

        [6,7,8,9,1,2,3,4,5] 3
        """
        n=len(nums)
        k=k%n
        def reverse(l,r):
            while l<r:
                nums[r],nums[l]=nums[l],nums[r]
                r-=1
                l+=1
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)
        
        
        