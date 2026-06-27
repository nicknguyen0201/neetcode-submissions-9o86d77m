from heapq import heappush, heappop, heapify
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
       
        
   
        min_heap = [(0,k)]
        neighbors=defaultdict(list)
        for [u,v,t] in times:

            neighbors[u].append((t,v))
        seen=set()
        min_cost=0
        while len(seen) < n and min_heap:
            t,v = heappop(min_heap)

            if v in seen:
                continue
                
            min_cost=max(min_cost,t)
            seen.add(v)
            for t_n,neighbor in neighbors[v]:
                if neighbor not in seen:
                    heappush(min_heap,(t_n+t,neighbor))
        if len(seen)==n:
            return min_cost
        return -1

    