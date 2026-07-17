class Solution:
    def integerBreak(self, n: int) -> int:
        """
        plan:
        assumption: k integers have to be identical
        common patter is /2 /3 /4 and try until the res//n=1
        WRONG, 10=4+3+3



        """
        dp = [0]*(n+1)
        dp[1]=1#only 1 way to break 1, base case
        for num in range(2,n+1):
            res=num if num!=n else 0
            for i in range(1,num):
                res=max(res,dp[i]*dp[num-i])
            dp[num]=res
        return dp[n]
        """
        dry run
        dp  1 2 3 4
            1 2 3 4
        num=4
        res=0
        i=1
        dp[1]*dp[3]=3
        dp[2]dp[2]=4

        
        """
