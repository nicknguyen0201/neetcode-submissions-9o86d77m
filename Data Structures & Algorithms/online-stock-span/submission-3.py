from collections import deque
class StockSpanner:

    def __init__(self):
        self.q=deque()
        self.idx=0
    def next(self, price: int) -> int:
        
        """
        maintain a monotonic stack always decreasing
        self idx=6
        start:[(100,0),(85,)]
        """
        if not self.q:
            self.q.append((price,0))
            return 1
        
        self.idx+=1
        while self.q:
            if price>= self.q[-1][0]: #today price>= past price
                self.q.pop()
            else:
                span=self.idx - self.q[-1][1]
                self.q.append((price,self.idx))
                return span
        self.q.append((price, self.idx))#if no one left, then this is the biggest we habe seen ever
        return self.idx+1 #index 2-0 is 2 but clearly we are larger than index 0,1 + ourselves

            

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
