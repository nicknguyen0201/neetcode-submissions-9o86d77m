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
        board = [['.']*n for _ in range(n)]
        self.count = 0
        delta_directions=[(0,-1), (-1, -1), (-1,0),(-1,1),(0,1),(1,1),(1,0), (1,-1)]

        def is_valid_square(r, c):
            if r<0 or r>=n:
                return False
            if c<0 or c>=n:
                return False
            return True
        def dfs(r,c,delta_index):
                nr, nc = r + delta_directions[delta_index][0], c + delta_directions[delta_index][1]
                if is_valid_square(nr, nc):
                    if board[nr][nc]=='Q':
                        return False
                    return dfs(nr,nc,delta_index)
                return True
        def is_valid_placement(row, col):
            for i in range (8):
                if dfs(row,col,i) == False:
                    return False
            return True

        def BT(row):
            if row >=n:
                self.count += 1
                return
            
            for col in range(n):
                if is_valid_placement(row, col):
                    board[row][col]='Q'
                    BT(row+1)
                    board[row][col]='.'
        BT(0)
        return self.count

        