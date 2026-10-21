class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """ in this probelm you have to keep track of 3 things ast the same time
        each tile of 9 tiles
        row 
        col

        """
        row_mp=defaultdict(set)
        col_mp=defaultdict(set)
        tile_mp=defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c]=='.': continue
                if board[r][c] in row_mp[r]:
                    return False
                if board[r][c] in col_mp[c]:
                    return False
                if board[r][c] in tile_mp[(r//3,c//3)]:
                    return False
                
                row_mp[r].add(board[r][c])
                col_mp[c].add(board[r][c])
                tile_mp[(r//3,c//3)].add(board[r][c])
        return True