class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        similar to unique path problem 
        build solution from bottom up
        """
        n=len(grid)
        m=len(grid[0])
        dp=[[0]*(m+1) for _ in range(n+1)]
        dp[n-1][m-1]=grid[n-1][m-1]
        #set end row and end col to inf
        for i in range(m+1):
            dp[n][i]=float('inf')
        for i in range(n+1):
            dp[i][m]=float('inf')
        for r in range(n-1,-1,-1):
            for c in range(m-1,-1,-1):
                if r==n-1 and c==m-1:
                    continue
                #dp[r][c]=min cost to get from this cell to the end
                dp[r][c]=grid[r][c]+ min(dp[r+1][c],dp[r][c+1])
        return dp[0][0]