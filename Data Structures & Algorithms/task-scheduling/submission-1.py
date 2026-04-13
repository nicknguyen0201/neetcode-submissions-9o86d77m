from collections import Counter, deque
from heapq import heappush, heappop
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        This give a heap vibe
        because with n cooldown 
        we can use a min heap to store what we can process next
        we can start with put the entire tasks into min heap
   
        Input: tasks = ["A","A","A","B","C"], n = 3
        time=8
        heap [,,]
        
        q->[]
        """
        mp=Counter(tasks)
        heap=[]
        for value in mp.values():
            heappush(heap,-value)
        q=deque()
        time=1

        while heap or q:
            
            if q:
                v,t = q[0]
                if t<=time:
                    heappush(heap, q.popleft()[0] )
            if heap: 
                #value is negative   
                value = heappop(heap)
                if value +1<0:
                    #if time=1, n=2, the earliest time I can do task is 4
                    q.append((value+1, time+1+n))
            time+=1
          
           

        return time-1


