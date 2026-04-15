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
        sort by start time 
        add to res find the next earliest start time 
        if start time later than current end time create new day?

        """
        intervals.sort(key=lambda x : x.start)
        heap=[]
        for interval in intervals:
            if heap and heap[0]<=interval.start:
                heappop(heap)
            heappush(heap, interval.end)
        return len(heap)