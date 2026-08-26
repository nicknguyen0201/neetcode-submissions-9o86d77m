from heapq import heappush, heappop
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        
        res={}
        h=[]
        i=0
        intervals.sort()
        n=len(intervals)
        for q in sorted(queries):
            while i<n and q>=intervals[i][0]:
                l,r=intervals[i][0], intervals[i][1]
                heappush(h,(r-l+1, r))
                i+=1
            while h and h[0][1]<q:
                heappop(h)
            if h:   
                res[q]=h[0][0] 
            else:
                res[q]=-1
                    

        return [res[q] for q in queries]