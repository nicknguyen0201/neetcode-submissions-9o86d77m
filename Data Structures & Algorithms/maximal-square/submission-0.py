class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        n=len(matrix)
        m=len(matrix[0])
        dp=[[0]*(m+1) for _ in range(n+1)]
        res=0
        for r in range(n-1,-1,-1):
            for c in range(m-1,-1,-1):
                if matrix[r][c]=="1":
                    dp[r][c]=1+min(dp[r+1][c],dp[r][c+1],dp[r+1][c+1])
                    res=max(res,dp[r][c]**2)
        return res

