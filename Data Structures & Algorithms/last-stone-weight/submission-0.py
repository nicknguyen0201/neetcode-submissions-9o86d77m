from heapq import heappush, heappop, heapify
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-x for x in stones]
        heapify(stones)
        while stones:
            s1 = -heappop(stones)
            if not stones:
                return s1
            s2 = -heappop(stones)
            res= s1-s2
            if res ==0 :
                if not stones:
                    return 0
                continue

            heappush(stones, -res)
        return 0
        