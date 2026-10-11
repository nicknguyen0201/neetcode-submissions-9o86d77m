from heapq import heappush, heappop
class MedianFinder:
    """
    Plan
    3>1
    1,3,2,4,5,6,3,3
    min heap: [3,4,5,6]

    max heap: [-3,-3,-2,-1]

    put first element in min heap
    if next el > min heap, put in max heap
    if next el < min heap, put in min heap
    if min heap size - maxheap size >1, move from max to min or vice versa
    return median (come from the larger heap) if both equal, return average


    """
    def __init__(self):
        self.bigheap=[] #store number bigger than its top
        self.smallheap=[] #store number smaller than top of the big heap
        

    def addNum(self, num: int) -> None:
        if not self.bigheap:
            heappush(self.bigheap, num)
        elif num>=self.bigheap[0]:
            heappush(self.bigheap, num)
            if abs(len(self.bigheap)-len(self.smallheap))>1:
                heappush(self.smallheap,-heappop(self.bigheap))
        else:
            heappush(self.smallheap, -num)
            if abs(len(self.bigheap)-len(self.smallheap))>1:
                heappush(self.bigheap,-heappop(self.smallheap))

    
    def findMedian(self) -> float:
        if len(self.bigheap)==len(self.smallheap):
            return (-self.smallheap[0]+self.bigheap[0])/2
        elif len(self.bigheap)>len(self.smallheap):
            return self.bigheap[0]
        else:
            return -self.smallheap[0]

