"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from heapq import heappush, heappop
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        
        """
        heap=[]
        intervals.sort(key = lambda x: x.start)
        for interval in intervals:
            if heap and interval.start >= heap[0]:#can we fit a meeting right now
                heappop(heap)
            heappush(heap,interval.end)
        return len(heap)