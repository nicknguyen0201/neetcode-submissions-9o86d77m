"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)#sort by end time
        for i in range(len(intervals)-1):
            start_now, end_now = intervals[i].start, intervals[i].end
            start_next, end_next = intervals[i+1].start, intervals[i+1].end
            if end_now > start_next:
                
                return False
        return True
