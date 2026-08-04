class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        """
        word1: ''
        word2: 'hello'
        5 insertions
            h   e    l   l   '' (w1)
        h                    5
        e                    4
        l                    3
        l            2   1   2
        o            2   1   1 (insertion ^) (replace diagonal)
        ''  4   3    2   1   0 (deletion <-)
        (w2)
        """ 
        dp =[[0]*(len(word1)+1) for _ in range(len(word2)+1)]
        for i in range(len(word1)+1):
            dp[len(word2)][i]=len(word1)-i
        for i in range(len(word2)+1):
            dp[i][len(word1)]=len(word2)-i
        for r in range(len(word2)-1,-1,-1):
            for c in range(len(word1)-1,-1,-1):
            
                if word1[c]==word2[r]:

                    dp[r][c]=min(dp[r+1][c+1],dp[r+1][c]+1, dp[r][c+1]+1)
                else:
                    dp[r][c]=min(dp[r+1][c+1]+1,dp[r+1][c]+1, dp[r][c+1]+1)

        return dp[0][0]