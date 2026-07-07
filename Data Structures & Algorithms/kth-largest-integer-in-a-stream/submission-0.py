from heapq import heappush, heappop, heapify
class KthLargest:
    """
    use a size k min heap
    where top is k-largest

    heap k [ -1,-2,-3 ]
    """
    def __init__(self, k: int, nums: List[int]):
        
        heapify(nums)
        while len(nums)>k:
            heappop(nums)
        self.minH=nums
        self.k=k
    def add(self, val: int) -> int:
        heappush(self.minH,val)
        if len(self.minH) >self.k:
            heappop(self.minH)
        return self.minH[0]

        
