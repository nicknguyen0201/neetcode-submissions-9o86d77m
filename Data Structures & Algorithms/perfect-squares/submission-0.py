class Solution:
    def numSquares(self, n: int) -> int:
        """
        understand(key assumptions)
        perfect square is the square of another int
        5^2=25, 25 is perfect square

        13 ->9 ->0: res=2
        13-4=9
        9-9=0
        DP

        Plan:
        Input: n = 13

        calculate which num are perfect square in
        range 13
        0, 1, 2, 3, 4, 5  6  7  8  9  10  11  12  13
        F. T. F. F. T. F. F  F  F. T. F.  F.  F.  F

        """

        dp=[n]*(n+1)
        dp[0]=0
        for target in range(1, n+1):
            for s in range(1,target+1):
                sq=s**2
                if target-sq<0:
                    break
                dp[target]=min(dp[target],dp[target-sq]+1)
        return dp[n]

