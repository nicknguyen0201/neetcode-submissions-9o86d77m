from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        @cache
        def BT(l,r):
            if l>r:
                return 0
            max_coin=0
            for i in range(l, r+1):
                left_ballon = 1 if l-1<0 else nums[l-1]
                right_ballon= 1 if r+1>=len(nums) else nums[r+1] 
                coin = left_ballon* nums[i] *right_ballon
                coin+= BT(l,i-1)+ BT(i+1,r)
                max_coin=max(max_coin, coin)
            return max_coin
        return BT(0, len(nums)-1)
