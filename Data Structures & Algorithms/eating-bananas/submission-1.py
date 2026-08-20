import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        1 4 3 2 pile h=9

        1 2 3 4 speed
          6 5     h=9
            l r   
            m

        """
        top_bound=max(piles)
        bot_bound=1
        def binsearch(l,r,h):
            res=r
            while l<=r:
                speed=(l+r)//2
                total_time=sum([math.ceil(pile/speed) for pile in piles ])
                if total_time<=h:
                    res=speed
                    #l=speed+1 we want to reduce speed,not max speed    
                    r=speed-1
                else:
                    #r=speed-1
                    l=speed+1
            return res
                    
        return binsearch(bot_bound,top_bound,h)