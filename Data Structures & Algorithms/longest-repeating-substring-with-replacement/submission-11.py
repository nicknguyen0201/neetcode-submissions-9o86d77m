class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        PlanL
        sliding window
        count to keep char freq inside our window
        a maxf for the max value inside count
         
        expand window until window size - maxf >k
        shrink window from left
        deduct freq
        update max window size 

        """
        res=l=maxf=0
        count={}

        for r in range (len(s)):
            c=s[r]
            count[c]=1+count.get(c,0)
            maxf=max(maxf,count[c])
            if r-l+1 - maxf>k:
                count[s[l]]-=1
                l+=1
            res=max(r-l+1,res)
        return res