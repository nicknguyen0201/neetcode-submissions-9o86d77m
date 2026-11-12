class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        high level overview
        insert interval
        merge when conflic 

        intervals[i]
        if not conflict new intervals
            put it to our result
        if  larger than our new interval
            add new interval add everyone else done
        
        if some conflict:
            merge inter i with new interval
        
            min(start,newInterval), max (end, newInterval)

        might not add the new interval alrrea
        add new interval
        return
        [[1,2],[3,5],[9,10]] [6,7]


        """
        result = []
        for i, [start, end] in enumerate(intervals):
            if end < newInterval[0]:
                result.append(intervals[i])
            elif start > newInterval[1]:
                result.append(newInterval)
                result += intervals[i:]
                return result
            else:
                newInterval[0] = min(start, newInterval[0])
                newInterval[1] = max(end, newInterval[1])
        result.append(newInterval)
        return result