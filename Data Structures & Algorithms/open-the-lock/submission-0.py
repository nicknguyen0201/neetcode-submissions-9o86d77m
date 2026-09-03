from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(comb):
            nbs=[]
            for i in range(4):
                digit=int(comb[i])
                nbs.append(comb[:i]+str((digit+1)%10)+comb[i+1:])
                nbs.append(comb[:i]+str((digit-1+10)%10)+comb[i+1:])
            return nbs
        if "0000" in deadends:
            return -1
        res=0
        visited=set(deadends)
        q=deque(["0000"])
        while q:

            for _ in range(len(q)):
                comb=q.popleft()
                if comb==target:
                    return res
                for nb in neighbors(comb):
                    if nb not in visited:
                        q.append(nb)
                        visited.add(nb)
            res+=1
        
        return -1

