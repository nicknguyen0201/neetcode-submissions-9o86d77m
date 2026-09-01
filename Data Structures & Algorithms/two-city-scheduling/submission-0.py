class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diffs=[(b-a,i) for i,[a,b] in enumerate(costs)]
        diffs.sort()
        res=0
        for i in range(len(costs)):
            if i<len(costs)//2:
                _,b=costs[diffs[i][1]]
                res+=b
            else:
                a,_=costs[diffs[i][1]]
                res+=a
        return res