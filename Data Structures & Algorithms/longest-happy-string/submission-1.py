from heapq import heappush, heappop,heapify

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        """
        one bad assumptions was I need to use all occurances of abc
        keep a prev variable, but allow it to go to 2

        a = 3, b = 4, c = 2
        maxH [[-2,b],[-1,a]]
        prev = [-2,a,1]
        res=bbaacc
        cnt,c,used=-2,c,1
        """
        
        maxH=[]
        if a:
            maxH.append([-a,'a'])
        if b:
            maxH.append([-b,'b'])
        if c:
            maxH.append([-c,'c'])
        heapify(maxH)
       
        res=''
        while maxH:
            cnt,c =heappop(maxH)
            if len(res)>=2 and res[-2]==res[-1]==c:
                if not maxH:
                    return res
                cnt2,c2=heappop(maxH)
                res+=c2
                cnt2+=1
                if cnt2!=0:
                    heappush(maxH,[cnt2,c2])
            else:
                res+=c
                cnt+=1
                if cnt==0:
                    continue
            heappush(maxH,[cnt,c])
        return res


        