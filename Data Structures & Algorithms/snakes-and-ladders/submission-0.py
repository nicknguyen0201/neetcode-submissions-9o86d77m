from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        """
        """
        n=len(board)
        
        board.reverse()
        visited=set()
        def jump_to(position):
            #-1 to round down, 12-1/2= row 1
            #8-1)%2=col 1
            row=(position-1)//n
            col=(position-1)%n
            #but if row is odd, col is flipped
            if row%2==1:
                col=n-1-col
            return board[row][col]
        
        q=deque([(1,0)])
        while q:
            cell,cost=q.popleft()
            for i in range(1,7):
                next_cell=i+cell
                if next_cell>n*n:
                    break
                jump_to_next_cell=jump_to(next_cell)
                if next_cell==n*n or jump_to_next_cell==n*n:
                    return cost+1
                elif jump_to_next_cell!=-1:
                    if jump_to_next_cell not in visited:
                        q.append((jump_to_next_cell,cost+1))
                        visited.add(jump_to_next_cell)
                else:
                    if next_cell not in visited:
                        q.append((next_cell,cost+1))
                        visited.add(next_cell)
        return -1

                