class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        output=[]
        row_len=len(heights)
        col_len=len(heights[0])
        visited_alt=[[False]*col_len for _ in range(row_len)]
        visited_pac=[[False]*col_len for _ in range(row_len)]
        def valid(r,c):
            return r<row_len and r>=0 and c<col_len and c>=0
        def dfs(r,c,visited):
            if visited[r][c]:
                return
            visited[r][c]=True
            for dr, dc in [(-1,0),(0,1),(1,0),(0,-1)]:
                nr,nc=dr+r,dc+c
                if valid(nr,nc) and heights[nr][nc]>=heights[r][c]:
                    dfs(nr,nc,visited)
            
        for col in range(col_len):
            if visited_pac[0][col]==False:
                dfs(0,col,visited_pac)
            if visited_alt[row_len-1][col]==False:
                dfs(row_len-1,col,visited_alt)

        for row in range(row_len):
            if visited_pac[row][0]==False:
                dfs(row,0,visited_pac)
            if visited_alt[row][col_len-1]==False:
                dfs(row,col_len-1,visited_alt)
        for row in range(row_len):
            for col in range(col_len):
                if visited_pac[row][col] and visited_alt[row][col]:
                    output.append([row,col])
        return output