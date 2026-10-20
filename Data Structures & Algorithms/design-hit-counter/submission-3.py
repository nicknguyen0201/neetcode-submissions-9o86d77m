from collections import deque
class HitCounter:

    def __init__(self):
        """
        wrong assumption: we might ask for hit at a past time stamp. eg: we are at time stamp 1500, and I want to know get hit timestamps(15)
        -solution based on wrong assumptionimplement a hashmap and a loop over 300 element from the timestamp backward to get the hit
        """
        self.q=deque()
    def hit(self, timestamp: int) -> None:
        self.q.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        while self.q:
            if self.q[0]+299<timestamp:
                self.q.popleft()
            else:
                break
        return len(self.q)



# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
