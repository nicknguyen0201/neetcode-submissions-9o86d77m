class Solution:
    def rob(self, nums: List[int]) -> int:
        #dp[i-2], dp[i-1] =0,0
        r_2, r_1 =0,0
        for num in nums:
            tmp = max(r_2+num,r_1)
            r_2=r_1
            r_1=tmp
        return r_1
        