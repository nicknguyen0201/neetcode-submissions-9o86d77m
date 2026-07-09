class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        sort by end point
        because it leaves more room for earlier interval
        """
        intervals.sort(key=lambda x:x[1])
        res=0
        prev_end = intervals[0][1]
        for i in range(1,len(intervals)):
            if prev_end<= intervals[i][0]:
                #non overlap, 
                prev_end=intervals[i][1]
            else:
                res+=1 #deleted this interval
        return res



