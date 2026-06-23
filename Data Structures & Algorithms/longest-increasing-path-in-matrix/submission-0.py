from functools import cache
class Solution:
   
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        @cache
        def BT(r,c):
            max_val = 0
            for dr, dc in [(-1,0),(0,1),(1,0),(0,-1)]:
                if r+dr>=0 and r+dr<len(matrix) and c+dc>=0 and c+dc<len(matrix[0]) and matrix[r+dr][c+dc]<matrix[r][c]:
                    travel = 1+BT(r+dr,c+dc)
                    max_val=max(max_val,travel)
            return max_val

        sr,sc=0,0
        max_val=0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                max_val = max(1+BT(r,c),max_val)

        return max_val
