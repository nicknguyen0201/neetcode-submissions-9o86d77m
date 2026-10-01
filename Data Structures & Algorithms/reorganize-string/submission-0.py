from heapq import heappush, heappop, heapify
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq=Counter(s)
        maxH=[(-cnt,c) for c,cnt in freq.items()]
        heapify(maxH)
        res=''
        prev=None
        while maxH or prev:
            if not maxH and prev:
                return ""
            cnt,c=heappop(maxH)
            res+=c
            cnt+=1

            if prev:
                heappush(maxH,prev)
                prev=None

            if cnt!=0:
                prev=(cnt,c)
        return res
