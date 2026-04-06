class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
            dynamic size window: win size - most count char inside window <= k
        [0, 1, 2, 3]
        """
        res =0
        l,r=0,0
        count={}
        n=len(s)
        maxf=0
        for r in range(n):
            c=s[r]
            count[c]=1+count.get(c,0)
            maxf = max(maxf,count[c])
            if ((r-l+1) - maxf >k): #invalid window. shrink left
                count[s[l]]-=1
                l+=1
            res=max(r-l+1,res)
        return res
