class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        high level overview
        things are sorted
        determine where new interval can start:
        - what if no overlap?
            when start of new interval > end time of previous one and new Interval end < start time next interval
            put the new interval here
            return

        - find first interval where there is overlap
            type 3: intervals i contain new intervals
            elif start new interval >= start i and end new interval<= end i

            type 1: end prev >= start of new interval
            [3,5],[4,10]
                    new
            type 2: end new interval with next start
            [3,5],[4,10]
            new

            min = 2 start time
            max = 2 end time
            keep checking if the new end is overlapping with any start after it
            max = 2 end time
      
        start=1
        end=10
        [[1,2],[3,6],[7,10]] + [2,8]
        res=[1,10]
        

        
        res=[]
        n=len(intervals)
        for i in range(n): #
            if intervals[i][1] < newInterval[0]:
                if i+1<n:
                    if newInterval[1] < intervals[i+1][0]:#new end < next start
                        res.append(newInterval)
                        res += intervals[i+1:]
                   
                else: #end of array
                    res.append(newInterval)
                return res
            elif intervals[i][0] <= newInterval[0] and intervals[i][1] >= newInterval[1]: #type 3                   
                return intervals
            else: # type 1 + 2 
                start = min(newInterval[0], intervals[i][0])
                end = max(newInterval[1], intervals[i][1])
                # loop check
                j = i + 1 #what if i+1 is out of bound
                while j < n:
                    if end >= intervals[j][0]:
                        end = max(end,intervals[j][1])
                        j+=1
                    else:
                        res += intervals[j+1:]
                        return res

                res.append([start,end])
                return res

        return res
        """
        res = []
        for i,interval in enumerate(intervals):
            start = interval[0]
            end = interval[1]
            if newInterval[0] > end: #end before new interval start
                res.append(interval)
            elif newInterval[1] < start:  #start before new interval end
                res.append(newInterval)
                res += intervals[i:]
                return res
            else:
                #some overlapping
                newInterval = [min(start,newInterval[0]),max(end, newInterval[1])]
        res.append(newInterval)
        return res
    
        