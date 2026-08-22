from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        def add_cell(r,c):
            if r<0 or c<0 or r>=len(grid) or c >=len(grid[r]):
                return 
            if grid[r][c]!=INF:
                return
            #guarding grid[r][c]==-2: this means we enque this alr, don't q again
            #guarding grid[r][c]==-1 or a vald distance too
            grid[r][c]=-2
            q.append((r,c))

        INF=2147483647
        q=deque()
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c]==0:
                    q.append((r,c))

        step=0
        while q:
            for _ in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=step
                for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:
                    add_cell(dr+r,dc+c)

            step+=1

