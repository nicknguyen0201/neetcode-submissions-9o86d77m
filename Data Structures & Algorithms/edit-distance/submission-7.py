class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """
        word2 →  (columns, j increasing →)
           m    o    n    k    e    y    s    .    
        m                                     5
        o                                     4
        n                                     3
        e                                2    2
        y                       2    1   1    1
        .   7    6    5    4    3    2   1    0

       word1 
        """
        dp=[[0]*(len(word2)+1) for _ in range(len(word1)+1)]
        cnt=0
        for j in range(len(word2),-1,-1):
            dp[len(word1)][j]=cnt
            cnt+=1
        cnt=0
        for i in range(len(word1),-1,-1):
            dp[i][len(word2)]=cnt
            cnt+=1
        for i in range(len(word1)-1,-1,-1):
            for j in range(len(word2)-1,-1,-1):
                if word1[i]==word2[j]:
                    dp[i][j]=dp[i+1][j+1]
                else:
                    dp[i][j]=1+min(dp[i+1][j+1],dp[i+1][j],dp[i][j+1])
        return dp[0][0]