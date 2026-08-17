class Solution:
    def validPalindrome(self, s: str) -> bool:
        time=0
        l,r=0,len(s)-1
        def dfs(l,r):
            
            substr=s[l:r+1]
            return substr==substr[::-1]
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                if time==0:
                    time+=1
                    res=dfs(l,r-1) or dfs(l+1,r)
                    if not res:
                        return False
                    return True
                else:
                    return False
        return True
        