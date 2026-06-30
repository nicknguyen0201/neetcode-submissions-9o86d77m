from heapq import heappush, heappop
class MedianFinder:
    """
    Plan
    min heap: 

    max heap:

    put first element in min heap
    if next el > min heap, put in max heap
    if next el < min heap, put in min heap
    if min heap size - maxheap size >1, move from max to min or vice versa
    return median (come from the larger heap) if both equal, return average

    """
    def __init__(self):
        self.max_heap=[]# store number smaller than min heap
        self.min_heap=[] # store bigger number than max heap
        

    def addNum(self, num: int) -> None:
        if not self.min_heap:
            heappush(self.min_heap, num)

        elif num >= self.min_heap[0]:
            heappush(self.min_heap,num)
            if abs(len(self.max_heap)-len(self.min_heap))>1:
                heappush(self.max_heap, - heappop(self.min_heap))

        else: 
            heappush(self.max_heap,-num)
            if abs(len(self.max_heap)-len(self.min_heap))>1:
                heappush(self.min_heap, - heappop(self.max_heap))
    
    def findMedian(self) -> float:
        if len(self.max_heap)==len(self.min_heap):
            return (-self.max_heap[0]+  self.min_heap[0])/2
        elif len(self.max_heap)>len(self.min_heap):
            return -self.max_heap[0]
        else:
            return self.min_heap[0]