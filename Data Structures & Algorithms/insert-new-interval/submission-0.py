class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        if start > new end: [2,4]  new end [0,1]
            safe to append the target interval 
        elif new start > end: new start: [ 3,5] >[ 0,2] #safe to insert the iterating interval
        
        else: conflict case new start<= end 
                            [3,5].      [2,4]
        """
        res=[]
        for i, interval in enumerate(intervals):
            if interval[0]> newInterval[1]:
                res.append(newInterval)
                return res+intervals[i:]
            elif interval[1]<newInterval[0]:
                res.append(interval)
            elif newInterval[0]<=interval[1]:
                newInterval=[min(newInterval[0],interval[0]),max(newInterval[1],interval[1])]
        res.append(newInterval)
        return res