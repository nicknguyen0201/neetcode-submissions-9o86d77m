class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        2 pass bin search
        first pass to identify the row the target is in

        2nd pass identify the col ther target id in
        """
        def binsearch(l,r,i):
            while l<r:
                m=(l+r)//2
                if matrix[m][i]>=target:
                    r=m
                else:
                    l=m+1
            return l
        def binsearch2(l,r,i):
            while l<=r:
                m=(l+r)//2
                if matrix[i][m]==target:
                    return True
                elif matrix[i][m]>target:
                    r=m-1
                else:
                    l=m+1
            return False
        #if len(matrix)==1:
            #return binsearch2(0,len(matrix[0])-1,0)
        row_idx=binsearch(0,len(matrix)-1,len(matrix[0])-1)
        return binsearch2(0,len(matrix[row_idx])-1,row_idx)
       