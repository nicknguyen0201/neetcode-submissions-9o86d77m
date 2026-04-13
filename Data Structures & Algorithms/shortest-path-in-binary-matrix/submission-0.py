class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """
        Understand:
        implement bfs
        Plan:
        visited set store tuplles
        keep a distance counter for each bfs level
        while queue
        

        """
        def check(nr,nc):
            return nr>=0 and nr<n and nc>=0 and nc<n
        n=len(grid)
        visited=set()
        if grid[0][0]==1:
            return -1
        q=deque([(0,0)])
        distance=0
        #direction up, up right, right, down right, down, down left, left, up left
        delta=[(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(-1,-1)]
        while q:
            level_len=len(q)
            distance+=1
            for _ in range(level_len):
                
                r,c = q.popleft()
                if r==n-1 and c==n-1:
                    return distance
                visited.add((r,c))
                for dr,dc in delta:
                    nr=dr+r
                    nc=dc+c
                    if check(nr,nc) and (nr,nc) not in visited and grid[nr][nc]==0:
                        q.append((nr,nc))
        return -1
            
        