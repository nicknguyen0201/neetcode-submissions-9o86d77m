class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_mp=defaultdict(set)
        row_mp=defaultdict(set)
        sq_mp=defaultdict(set)
        for r in range( 9):
            for c in range(9):
                if board[r][c]=='.':
                    continue
                if board[r][c] in col_mp[c]:
                    return False
                if board[r][c] in row_mp[r]:
                    return False
                if board[r][c] in sq_mp[(r//3,c//3)]:
                    return False
                
                col_mp[c].add(board[r][c])
                row_mp[r].add(board[r][c])
                sq_mp[(r//3,c//3)].add(board[r][c])
        return True