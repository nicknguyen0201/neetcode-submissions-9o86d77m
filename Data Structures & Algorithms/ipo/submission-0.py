from heapq import heappush, heappop, heapify
class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        """
        min heap (capital, profit, )
        min heap put a project into the heap so you get the most affordable one

        max heap (profit)
        max heap pop from top heap to get project give you most profit

        """
        min_heap = [(cap, profit) for cap, profit in zip(capital, profits)]
        heapify(min_heap)

        max_heap = []
        res = 0

        for _ in range(k):
            while min_heap and min_heap[0][0]<=w: # can we afford the project
                cap, profit = heappop(min_heap)
                heappush(max_heap, -profit )
            
            # we have gotten all projects we can afford this round, let's pick one to build
            if not max_heap:
                break #in case we can't afford any project
            w += -heappop(max_heap)
         
        return w


