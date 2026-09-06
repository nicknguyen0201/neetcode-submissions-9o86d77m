class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.ROWS=len(matrix)
        self.COLS=len(matrix[0])
        self.prefix_mat=[[0]*(self.COLS+1) for _ in range(self.ROWS+1)]
        for r in range(self.ROWS):
            prefix=0
            for c in range(self.COLS):
                prefix+=matrix[r][c]
                above=self.prefix_mat[r][c+1]
                self.prefix_mat[r+1][c+1]=prefix+above
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1,c1,r2,c2=row1+1,col1+1,row2+1,col2+1
        topleft=self.prefix_mat[r1-1][c1-1]
        botleft=self.prefix_mat[r2][c1-1]
        botright=self.prefix_mat[r2][c2]
        topright=self.prefix_mat[r1-1][c2]
        return topleft + botright-botleft-topright


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)