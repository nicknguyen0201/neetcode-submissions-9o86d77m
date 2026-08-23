class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def valid(r,c):
            return r>=0 and r<len(board) and c>=0 and c<len(board[r]) and board[r][c]=='O'
        def dfs(r,c):
            if not valid(r,c):
                return
            board[r][c]='T'
            for dr,dc in [(-1,0),(0,1),(1,0),(0,-1)]:
                dfs(r+dr,c+dc)
            
        for r in range(len(board)):
            dfs(r,0)
            dfs(r,len(board[r])-1)
        for c in range(len(board[0])):
            dfs(0,c)
            dfs(len(board)-1,c)
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c]=='O':
                    board[r][c]='X'
                elif board[r][c]=='T':
                    board[r][c]='O'
        