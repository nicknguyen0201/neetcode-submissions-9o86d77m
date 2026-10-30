"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        """
        check add all meeting
        sort by start time
        iterate to check:
            i
                         s1 e1. s2 e2
            (0,5),(5,10),(15,20)

        intervals.sort()
        for i in range(len(intervals) - 1):
            start1, end1 = intervals[i]
            start2, end2 = intervals[i+1]
            if end2 < end1:#second interval is contained by 1st
                return False
            elif start2 < end1: #half contained by 1st interval
                return False
        return True
        """
        intervals.sort( key = lambda x: x.start)
        for i in range(len(intervals) - 1):
            start1, end1 = intervals[i].start,intervals[i].end
            start2, end2 = intervals[i+1].start,intervals[i+1].end
            if end2 < end1:#second interval is contained by 1st
                return False
            elif start2 < end1: #half contained by 1st interval
                return False
        return True