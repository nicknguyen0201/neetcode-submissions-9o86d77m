from heapq import heappush, heappop, heapify
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        """

        head =.  (total processing time, idx)
        """
        pending=[(enqueue,i,process) for i,[enqueue,process] in enumerate(tasks)]
        heapify(pending)
        available=[]
        res=[]
        time=0
        while pending or available:
            
            while pending and pending[0][0]<=time:

                heappush(available,(pending[0][2],pending[0][1]))
                heappop(pending)
            if not available:
                time=pending[0][0]
                continue
            if available:
                time+=available[0][0]
                res.append(heappop(available)[1])
        return res