class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        sort by start
        iterate 
        check i, i+1
        if not overlap
            append i to res
        if overlap
            update min and max of start and end carry to next interval
        """
        intervals.sort(key = lambda x: x[0])
        def is_overlap(a,b):
            return a[1]>=b[0]
        res=[]
        for i in range(len(intervals)-1):

            if not is_overlap(intervals[i],intervals[i+1]):
                res.append(intervals[i])
            else:
                intervals[i+1]=[min(intervals[i][0],intervals[i+1][0]), max(intervals[i][1],intervals[i+1][1])]
        res.append(intervals[len(intervals)-1])
        return res