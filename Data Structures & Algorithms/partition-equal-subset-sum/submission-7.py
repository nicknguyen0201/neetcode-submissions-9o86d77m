class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """given a target, nums:
        determine if you can get to target given the nums


            1,  2,  3,  4   target=5

            0   1   2   3   4   5
            T   F   F   F
        1   T   T   F   F
        2   T   T   T   F
        3   T   T   T   T   T   T
        4   T   T   T   T   T   T
        """
        if sum(nums)%2!=0:
            return False
        target=sum(nums)//2
        n=len(nums)
        dp=[False]*(target+1)
        nextdp=[False]*(target+1)
        dp[0]=True
        for num in nums:
            for j in range (1,target+1):
                if j-num>=0:
                    nextdp[j]=max(dp[j],dp[j-num])
                else:
                    nextdp[j]=dp[j]
            dp,nextdp=nextdp,dp
   
        return dp[target]
                
        