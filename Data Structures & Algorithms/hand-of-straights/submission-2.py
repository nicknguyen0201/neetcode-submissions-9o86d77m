from collections import Counter
from heapq import heappush, heappop, heapify
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize!=0:
            return False
        
        freq = Counter(hand)
        minH = [x for x in freq.keys()]
        heapify(minH)
        while minH:
            min_num = minH[0]
            
            #check a window 
            for num in range(min_num, min_num +groupSize):
                if freq[num]<=0:
                    return False
                
                freq[num]-=1

                if freq[num]==0:
                    if minH[0]!=num:
                        return False
                    heappop(minH)
                    
        return True






        
