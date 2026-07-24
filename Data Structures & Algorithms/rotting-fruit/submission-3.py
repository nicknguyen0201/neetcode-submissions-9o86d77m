from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        level-order bfs
        """
        q=deque()
        fresh=0
        for r in range(len(grid)):
            for c in range(len(grid[r])):
                if grid[r][c]==2:
                    q.append((r,c))
                elif grid[r][c]==1:
                    fresh+=1
        #seen=set()
        #forgoten edge case
        if fresh==0:
            return 0#0 time to process 0 rotten fruit
        time=-1
        while q:#1
            level_len=len(q)#1
            for _ in range(level_len):
                r,c=q.popleft() #2,2
                #seen.add(node)
                for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:
                    nr,nc=dr+r,dc+c
                    if nr<0 or len(grid)<=nr or nc<0 or len(grid[nr])<=nc:
                        continue
                    if grid[nr][nc]==2 or grid[nr][nc]==0:
                        continue
                    q.append((nr,nc))
                    fresh-=1
                    grid[nr][nc]=2#rotten
            time+=1
        return time if fresh==0 else -1
                    


