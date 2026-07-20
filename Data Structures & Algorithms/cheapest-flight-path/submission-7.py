class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """
        prices: keep track of current state of cost to get to somewhere in current k
        tmp_prices: update the new prices
        we have to ensure the prices do not see any path that meant for next k it not supposed to know

        """
        prices=[float('inf')]*n
        prices[src]=0
        for i in range(k+1):
            tmp=prices.copy()
            for s,d,p in flights:
                if prices[s]==float('inf'):
                    continue #we can't get to this airport yet 
                if prices[s]+p<tmp[d]:
                    tmp[d]=prices[s]+p# if we can get to s and +p give
            prices=tmp
        return -1 if prices[dst]==float('inf') else prices[dst]