from collections import deque
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def valid(r,c):
            return r>=0 and r<len(grid) and c>=0 and c<len(grid[r]) 
        directions=[(-1,0),(0,1),(1,0),(0,-1)]
        q=deque()
        for r in range(len(grid)):
            found=False
            for c in range(len(grid[r])):
                if grid[r][c]==1:
                    q.append((r,c))
                    grid[r][c]=-1
                    found=True
                    break
            if found:
                break
        peri=0

        while q:
            r,c=q.popleft()
            node_peri=4
            for dr,dc in directions:
                nr,nc=dr+r,dc+c
                if valid(nr,nc):#each not out of bound square +1 peri
                    if grid[nr][nc]==-1:#visited neighbor
                        node_peri-=1
                    elif grid[nr][nc]==1:#neighbor can be visited
                        q.append((nr,nc))
                        grid[nr][nc]=-1
                        node_peri-=1
            peri+=node_peri
        return peri


        



