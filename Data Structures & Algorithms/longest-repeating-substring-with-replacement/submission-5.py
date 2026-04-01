from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        U: 
        XYYYX , k=2 -> XXXYX result is 3
                    -> YYYYY 5
        this suggest we can keep a counter to increment the count
        and then start from the candidate with highest count down to the candidate with lowest count
         O(N^2)
        """
        charSet=set(s)
        res=0
        #if we can make a window consist of all of this char
        for c in charSet:
            count=0
            l=0
            #makig the window
            for r in range(len(s)):
                if s[r]==c:
                    count+=1
                while r-l+1 -count >k:
                    if s[l]==c:
                        count-=1
                    l+=1
                res=max(res,r-l+1)
        return res


