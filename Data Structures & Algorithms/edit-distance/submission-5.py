from functools import cache
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp =[[0]*(len(word2)+1) for _ in range(len(word1)+1)]

        for i in range(len(word1),-1,-1):
            for j in range(len(word2),-1,-1):
                if i==len(word1) and j==len(word2):
                    continue
                elif i<len(word1) and j==len(word2):
                    dp[i][j]=1+ dp[i+1][j]
                elif j<len(word2) and i==len(word1):
                    dp[i][j]=1+dp[i][j+1]
                elif word1[i]==word2[j]:
                    dp[i][j]=dp[i+1][j+1]
                else:
                    dp[i][j]=1+min(dp[i+1][j+1],dp[i][j+1],dp[i+1][j])
        return dp[0][0]
