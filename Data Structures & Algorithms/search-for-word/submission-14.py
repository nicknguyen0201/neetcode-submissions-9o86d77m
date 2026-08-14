class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """

        O(n^2 * 4^m)
        """
        def valid(r,c):
            return r>=0 and c>=0 and r<len(board) and c<len(board[r])

        dir=[(-1,0),(0,1),(1,0),(0,-1)]

        def BT(r,c,i):
            
            if board[r][c]=='#': #explored
                return False
            
            if board[r][c]!=word[i]:
                return False
            if i==len(word)-1:
                return True
            
            tmp=board[r][c]
            board[r][c]='#'
            for dr, dc in dir:
                nr,nc=dr+r,dc+c
                if valid(nr,nc):
                    if BT(nr,nc,i+1):
                        board[r][c]=tmp#restore once sucess
                        return True
            board[r][c]=tmp
            return False


        for r in range(len(board)):
            for c in range(len(board[0])):
                if BT(r,c,0):
                    return True
                
        return False
                