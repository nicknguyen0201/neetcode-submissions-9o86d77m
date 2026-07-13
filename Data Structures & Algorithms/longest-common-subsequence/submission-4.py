class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """ 0.  1.   2  3.   4.   5
            c   r   a   b    t   
        c   3           1    1     
        a       2   2   1    1    0
        t           1   1    1    0
            0   0   0   0    0    0

        """
        dp=[[0]*(len(text2)+1) for _ in range(len(text1)+1)]
        for i in range(len(text1)-1,-1,-1):
            for j in range(len(text2)-1,-1,-1):
                if text1[i]==text2[j]:
                    dp[i][j]=dp[i+1][j+1]+1
                else:   
                    dp[i][j]=max(dp[i+1][j],dp[i][j+1])
        return dp[0][0]

