class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def valid(r,c):
            return r>=0 and r<n and c<n and c>=0
        def safe(r,c):
            for dr,dc in directions:
                nr,nc=dr+r,dc+c
                while valid(nr,nc):
                    if grid[nr][nc]=='Q':
                        return False
                    nr+=dr
                    nc+=dc
            return True
        def BT(r):
            if r==n:
                grid_copy=["".join(row) for row in grid]
                res.append(grid_copy)
                return 

            for c in range(n):
                if safe(r,c):
                    grid[r][c]='Q'
                    BT(r+1)
                    grid[r][c]='.'
        res=[]
        #note that we never place 2 queen in a row, so we only need 6 directions
        directions=[(-1,0),(-1,1),(1,1),(1,-1),(0,-1),(-1,-1)]   
        grid=[["."]*n for _ in range(n)]
        BT(0)
        return res
            
                
        