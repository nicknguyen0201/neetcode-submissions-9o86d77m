class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
             [
             [1,4],[2,3], [3,4]
             ]
        """
        intervals.sort(key = lambda x: x[0])
        _, prev_end = intervals[0]
        res = 0
        for start, end in intervals[1:]:
            if start >= prev_end:
                #no overlap, move to take on this interval
                prev_end = end
            else:
                res += 1
                #delete the interval end later because 
                #it gives more chance for later interval
                # to not overlap
                prev_end = min(end, prev_end)
        return res