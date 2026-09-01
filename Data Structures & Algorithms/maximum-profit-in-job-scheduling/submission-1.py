import bisect
from functools import cache
class Solution:
  
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        res=0
        intervals=sorted(zip(startTime,endTime,profit))
    
        @cache
        def BT(i):
            if i>=len(intervals):
                return 0
            skip =BT(i+1)
            j=bisect.bisect(intervals,(intervals[i][1],-1,-1))
            take = intervals[i][2]+BT(j)
            res=max(skip,take)
            return res

        
        return BT(0)