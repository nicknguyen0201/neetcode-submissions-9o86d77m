class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """

      
        """
        atl=set()
        pac=set()
        def dfs(r,c,visited):
            if (r,c) in visited:
                return
            visited.add((r,c))
            for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:
                nr,nc=r+dr,c+dc
                if nr<0 or nr>=len(heights) or nc<0 or nc>=len(heights[r]):
                    continue
                #are we going equal or uphill in elevation
                if heights[r][c]<=heights[nr][nc]:
                    dfs(nr,nc,visited)
                    
        for c in range(len(heights[0])):
            dfs(0,c,pac)
            dfs(len(heights)-1,c,atl)
        for r in range(len(heights)):
            dfs(r,0,pac)
            dfs(r, len(heights[r])-1,atl)
        return list(atl&pac)

                