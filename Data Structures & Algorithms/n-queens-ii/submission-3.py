class Solution:
    def totalNQueens(self, n: int) -> int:
        """
        plan:
        
        have a check function to check 8 directions of queen attack

        have a board graph nxn 

        have a global count

        def dfs(row):
            base:
            if row out of bound >=n:
                count += 1
                return
            for col in range n:
                if is_valid_placement(row, col)
                    board[row][col]=Q
                    dfs(row+1)
                    board[row][col]=.
        """
        
        """
        delta_directions=[(0,-1), (-1, -1), (-1,0),(-1,1),(0,1),(1,1),(1,0), (1,-1)]

        def is_valid_square(r, c):
            if r<0 or r>=n:
                return False
            if c<0 or c>=n:
                return False
            return True
        def dfs(r,c,delta_index):#O(N)
                nr, nc = r + delta_directions[delta_index][0], c + delta_directions[delta_index][1]
                if is_valid_square(nr, nc):
                    if board[nr][nc]=='Q':
                        return False
                    return dfs(nr,nc,delta_index)
                return True
        def is_valid_placement(row, col): #run O(n)
            for i in range (8):
                if dfs(row,col,i) == False:
                    return False
            return True
        """
        #board = [['.']*n for _ in range(n)]
        self.count = 0
        occupied_cols= set()
        positive_diag = set()
        negative_diag = set()

        def is_valid_placement(r, c):
            if r-c in negative_diag:
                return False
            if r+c in positive_diag:
                return False
            if c in occupied_cols:
                return False
            return True

        def BT(row):
            if row >=n:
                self.count += 1
                return
            for col in range(n):#0,1,2...n
                if is_valid_placement(row, col):# O(1) each time
                    #board[row][col]='Q'
                    negative_diag.add(row - col)
                    positive_diag.add(row + col)
                    occupied_cols.add(col)
                    BT(row+1)#0,1,2,..,n
                    #board[row][col]='.'
                    negative_diag.remove(row - col)
                    positive_diag.remove(row + col)
                    occupied_cols.remove(col)
        BT(0)
        return self.count

        