class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        plan
        use nested for loop to find starting char
        run bt on that char
        
        bt with path set of tuple
        so we don't use the same path


        """
        def valid(nr,nc):
            return nr>=0 and nr<row_len and nc>=0 and nc<col_len
        def BT(start,row,col):
            if start==len(word):
                return True
            for dr, dc in [(-1,0),(0,1),(1,0),(0,-1)]:
                nr,nc=row+dr,col+dc
                if valid(nr,nc) and (nr,nc) not in seen and board[nr][nc]==word[start]:
                    seen.add((nr,nc))
                    res = BT(start+1,nr,nc)
                    if res:
                        return True
                    seen.remove((nr,nc))
            return False

        row_len=len(board)
        col_len=len(board[0])
        seen=set()
        if not word:
            return True
        for r in range(row_len):
            for c in range(col_len):
                if board[r][c]==word[0]:
                    seen.add((r,c))
                    res = BT(1,r,c)
                    
                    if res:
                        return True
                    seen.remove((r,c))
        return False
        

        
