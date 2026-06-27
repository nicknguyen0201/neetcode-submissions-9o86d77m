from heapq import heappush, heappop, heapify
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
       
        
        """
        min_heap = [(0,k)]
        neighbors=defaultdict(list)
        for [u,v,t] in times:

            neighbors[u].append((t,v))
        seen=set()
        min_cost=0
        while len(seen) < n and min_heap:
            t,v = heappop(min_heap)
            min_cost=max(min_cost,t)
            seen.add(v)
            for t_n,neighbor in neighbors[v]:
                if neighbor not in seen:
                    heappush(min_heap,(t_n+t,neighbor))
        if len(seen)==n:
            return min_cost
        return -1"""

    
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        minHeap = [(0, k)]
        visit = set()
        t = 0
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = w1

            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        return t if len(visit) == n else -1


