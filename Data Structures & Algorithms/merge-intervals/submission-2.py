class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
            sort by start time
            
            res =[]
            for interval in interval
                if the res list empty:
                    add
                elif conflict with res[-1]:
                    res[-1][0] = min
                    res[-1][1] = max
                else:
                    add
        conflict cases
        1 3 vs 2 4 start <= res[-1][1]
        1 3 vs 1 4  res[-1][1] <= end
        1 3 vs 1 2
        """
        intervals.sort( key = lambda x : x[0])
        res = []
        for start, end in intervals:
            if not res:
                res.append([start,end])
            elif start <= res[-1][1]:
                res[-1][0] = min(start, res[-1][0])
                res[-1][1] = max(res[-1][1], end)
            else:
                res.append([start,end])
        return res
