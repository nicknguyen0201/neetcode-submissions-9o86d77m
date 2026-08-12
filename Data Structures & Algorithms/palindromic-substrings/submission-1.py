class Solution:
    def countSubstrings(self, s: str) -> int:
        def explore(l,r):
            res=0
            while l>=0 and r<len(s) and s[l]==s[r]:
                res+=1
                l-=1
                r+=1
            return res
        total=0
        for i in range(len(s)):
            if i==len(s)-1:
                total+=explore(i,i)
                continue
            total+=explore(i,i)
            total+=explore(i, i+1)
        return total