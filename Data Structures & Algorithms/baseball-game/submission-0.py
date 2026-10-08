class Solution:
    def calPoints(self, operations: List[str]) -> int:
        s=[]
        for c in operations:
            if c=="C":
                s.pop()
            elif c=="D":
                s.append(s[-1]*2)
            elif c=="+":
                s.append(s[-1]+s[-2])
            else:
                s.append(int(c))
        return sum(s)
