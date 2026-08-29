class CountSquares:

    def __init__(self):
        self.pts=[]
        self.mp=defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.mp[(point[0],point[1])]+=1
        self.pts.append(point)
    def count(self, point: List[int]) -> int:
        px,py=point
        res=0
        for x,y in self.pts:
            if abs(px-x)==abs(py-y) and px!=x and py!=y:
                res+=self.mp[(x,py)]*self.mp[(px,y)]
        return res
