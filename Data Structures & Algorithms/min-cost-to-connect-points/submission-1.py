from heapq import heappush, heappop, heapify
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #calculate all possible pair distance
        costs=defaultdict(list)
        for xi, yi in points:
            for xj,yj in points:
                if xi==xj and yi==yj:
                    continue
                cost = abs(xi-xj)+abs(yi-yj)
                costs[(xi,yi)].append((cost, xj,yj))
        
        seen=set()
        total=0
        heap=[(0, points[0][0], points[0][1])]#xi,yi
        while heap:
            cost, xi,yi = heappop(heap)
            if (xi,yi) in seen:
                continue
            total+=cost
            seen.add((xi,yi))
            for cost, xj, yj in costs[(xi,yi)]:
                if (xj,yj)not in seen:
                    heappush(heap, (cost, xj,yj))
         
        return total

