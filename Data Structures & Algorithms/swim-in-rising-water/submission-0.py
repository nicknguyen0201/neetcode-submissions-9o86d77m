from heapq import heappush, heappop
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        this is dijstrka b/c we have src, dst and goal is to find path where the max height of any 
        nodes are smallest

        """
        heap=[(grid[0][0],0,0) ]
        seen=set()


        while heap:
            cost, r,c =heappop(heap)
            if r==len(grid)-1 and c==len(grid[0])-1:
                return cost
            if (r,c) in seen:
                continue
            seen.add((r,c))
            for dr, dc in [(-1,0),(0,1),(1,0),(0,-1)]:

                nr,nc = r+dr, c+dc
                if nr>=0 and nr<len(grid) and nc>=0 and nc<len(grid[0]) and (nr,nc) not in seen:
                    heappush(heap,( max(cost,grid[nr][nc]),nr,nc    ) )


