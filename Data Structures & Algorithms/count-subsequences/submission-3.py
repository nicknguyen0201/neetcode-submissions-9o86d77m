class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """
            c   a   a   a   t _(s)
        c   3   0   0   0   0   0
        a   3   3   2   1   0   0
        t   1   1   1   1   1   0    
        _   1   1   1   1   1   1
        (t)


        """
        row =len(t)
        col=len(s)
        dp=[[0]*(col+1) for _ in range(row+1)]

        for i in range(col+1):
            dp[row][i]=1

        for i in range(row-1,-1,-1):
            for j in range(col-1,-1,-1):
                dp[i][j]=dp[i][j+1]
                if t[i]==s[j]:
                    dp[i][j]+=dp[i+1][j+1]
        return dp[0][0]
