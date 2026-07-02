class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total=0
        res=0
        if sum(gas) < sum(cost):
            return -1
        for i, g in enumerate(gas):
            c=cost[i]
            total+=g
            total-=c
            if total<0:
                total=0
                res=i+1
        return res