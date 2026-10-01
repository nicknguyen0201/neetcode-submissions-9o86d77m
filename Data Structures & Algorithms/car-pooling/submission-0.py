from heapq import heappush,heappop
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        assumptions 1
        can you combine passenger if capacity allow, like bus pick up more ppl at a bus stop
        ans : yes

        sort by pick up time
        heap store drop off time

        at drop off time drop off all ppl, subtract from capacity
        alternate between drop off and pick up?
        No, for every pick up location, we calculate drop off before letting new ppl come on
        """
        h=[]
        curr_cap=0
        trips.sort(key=lambda x: x[1])
        for cnt, pickup,dropoff in trips:
            if h:
                while h and h[0][0]<=pickup:
                    curr_cap-=heappop(h)[1]  
            if curr_cap+cnt<=capacity:
                heappush(h,(dropoff,cnt))
                curr_cap+=cnt
            else:
                return False
        return True



