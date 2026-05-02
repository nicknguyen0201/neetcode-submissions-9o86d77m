from heapq import heappush,heappop

class MedianFinder:
    """
    understand:
    to constantly keep track of a middle value in a stream
    there need to be some sorting such that we know who is middle
    1 min heap and 1 max heap
    
    the max heap store sorted upward from left
    if you smaller than left heap, go there
    1
    2
    the min heap store sorted downward from right half
    if you larger than right heap, go there
    """
    def __init__(self):
        self.leftheap=[]#maxheap
        self.rightheap=[]#minheap

    def addNum(self, num: int) -> None:
        if not self.leftheap:
            heappush(self.leftheap,-num)
        elif num>-self.leftheap[0]:
            heappush(self.rightheap,num)
        else:
            heappush(self.leftheap,-num)
        if abs(len(self.leftheap)-len(self.rightheap))>1:
            if len(self.leftheap)>len(self.rightheap):
                x=-heappop(self.leftheap)
                heappush(self.rightheap,x)
            else:
                x=heappop(self.rightheap)
                heappush(self.leftheap,-x)

    def findMedian(self) -> float:
        if (len(self.leftheap)+len(self.rightheap))%2==0:
            return (-self.leftheap[0]+self.rightheap[0])/2.0
        elif len(self.leftheap)>len(self.rightheap):
            return -self.leftheap[0]
        else:
            return self.rightheap[0]
        