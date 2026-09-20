from heapq import heappush,heappop
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        h=[]
        heappush(h,(0,0,0))
        visited=set()
        directions=[(-1,0),(0,1),(1,0),(0,-1)]
        def valid(r,c):
            return r>=0 and r<len(heights) and c>=0 and c<len(heights[0]) and (r,c) not in visited
        
        while h:
            diff, row, col=heappop(h)
            if row==len(heights)-1 and col ==len(heights[0])-1:
                return diff
            if (row,col) in visited:
                continue
            visited.add((row,col))
            for dr,dc in directions:
                nr,nc=row+dr,col+dc 
                if valid(nr,nc):
                    new_diff=max(diff,abs(heights[nr][nc]-heights[row][col]))
                    heappush(h,(new_diff,nr,nc))

            
