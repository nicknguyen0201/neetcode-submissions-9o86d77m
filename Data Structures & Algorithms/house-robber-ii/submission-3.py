class Solution:
    def rob(self, arr: List[int]) -> int:
        
        def max_rob(nums):
            n=len(nums)
            if n==2:
                return max(nums[0],nums[1])
            dp=[0]*n
            dp[n-1]=nums[n-1]
            dp[n-2]=max(nums[n-2],nums[n-1])
            for i in range(n-3,-1,-1):
                dp[i]=max(dp[i+1],nums[i]+dp[i+2])
            return dp[0]
        
        if len(arr)==1:
                return arr[0]
        if len(arr)==2: 
            return max(arr[0],arr[1])
        return max(max_rob(arr[1:]),max_rob(arr[:-1]))