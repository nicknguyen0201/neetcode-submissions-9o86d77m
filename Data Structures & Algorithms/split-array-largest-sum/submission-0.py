class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        """
            slide in k-1 walls between nums such that any 
            subarr is minimal

            the minimal sum can never be any smaller than min(nums)
            and can never be any larger than sum(nums)

            [2, 4, 10, 1, 5]
        min = 10
        max = 22
        mid= 16 
        l=14
        r=16
        """
        def can_partition(value , walls ):
            sum = 0
            k = 1
            for num in nums:
                sum += num 
                if sum > value:
                    sum = num
                    k += 1
            return k <= walls

        left, right = max(nums), sum(nums)
        while left < right:
            mid = left + (right - left) // 2
            if can_partition(mid,k):
                right = mid 
            else:
                left = mid + 1
        return right
        