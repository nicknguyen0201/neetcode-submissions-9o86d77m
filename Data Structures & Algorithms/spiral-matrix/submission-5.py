class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        steps=[len(matrix[0]),len(matrix)-1]
        d,r,c=0,0,-1
        directions = [(0,1),(1,0),(0,-1),(-1,0)]
        while steps[d&1]:
            dr,dc = directions[d]
            for _ in range(steps[d&1]):
                r+=dr
                c+=dc
                res.append(matrix[r][c])
            steps[d&1]-=1
            d+=1
            d%=4
        return res