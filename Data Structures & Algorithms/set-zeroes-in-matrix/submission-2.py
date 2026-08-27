class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        01
        11
        """
        first_row_zero=False
        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                if matrix[r][c]==0:
                    matrix[0][c]=0
                    if r==0:
                        first_row_zero=True
                        
                    else:
                        matrix[r][0]=0

        for r in range(1,len(matrix)):
            for c in range(1,len(matrix[r])):
                if matrix[0][c] ==0 or matrix[r][0]==0:
                    matrix[r][c]=0
        for r in range(len(matrix)):
            if matrix[0][0]==0:
                matrix[r][0]=0
        if first_row_zero:
            for c in range(len(matrix[0])):
                matrix[0][c]=0
