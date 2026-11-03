from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        BFS 
        modify inplace, so no extra mem for hashset, but still mn for queue

        for loop
            for loop
                when see 1, run bfs, 

        """
        directions=[(0,-1),(-1,0),(0,1),(1,0)]
        def is_valid(row, col):
            if row < 0 or row >= len(grid):
                return False
            if col < 0 or col >= len(grid[row]):
                return False
            if grid[row][col] == '0':
                return False
            return True

        def BFS(row, col):
            queue=deque([(row, col)])
            grid[row][col]='0'
            while queue:
                r, c = queue.popleft()
                for delta_row, delta_col in directions:
                    new_row, new_col = r + delta_row, c + delta_col
                    if is_valid(new_row, new_col):
                        grid[new_row][new_col] = '0'
                        queue.append((new_row,new_col))
        island_count=0            
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                if grid[row][col] == '1':
                    BFS(row,col)
                    island_count += 1
        return island_count


