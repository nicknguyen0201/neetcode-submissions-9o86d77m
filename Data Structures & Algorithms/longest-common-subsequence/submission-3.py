class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
            b  a  t
        c 

        r

        a

        b

        t

        """
        n1=len(text1)
        n2=len(text2)
        dp=[[0]*(n1+1) for _ in range(n2+1)]
        
        for r in range(n2-1, -1,-1):
            for c in range (n1-1,-1,-1):
                if text2[r]==text1[c]:
                    dp[r][c]= 1 + dp[r+1][c+1]
                else:
                    dp[r][c] = max(dp[r+1][c],dp[r][c+1])
        return dp[0][0]