from functools import cache
class Solution:
    """
    @cache
    def isMatch(self, s: str, p: str) -> bool:
        
        high level overview
        this is a recursive/backtracking 
        where we try different ways to get to end of s and p at the same time

        plan
        base case get to end of s and p at the same time return true
        get to end of 1 out of 2, return false
        isMathch(s,p)
        parse 1 to 1 from s and p
    
        
        if p[i+1]followed by *: we can recurse indefinitely
        if isMatch(s[i+1:],p[i:])
            return True
        #also we can choose to not recurse anymore
        return isMatch(s[i],p[i+2])

        else:
            
            if s[i] not p[i] and pi not . return false
            return recurse(i+1,i+1)
        
        isMatch(s, p)
        s = "x  y   z"
        p = ".  *   z "
             
            isMatch(yz,.*z)
                isMatch(z,.*z)
                    isMatch('',.*z)False 
                    isMatch()
    
        #base cases
        if len(s) == 0 and len(p) == 0:
            return True
        if len(p) == 0:
            return False #because len(s) is not 0

        if 1 < len(p) and p[1] == '*':
            if len(s) > 0 and (p[0] == s[0] or p[0] == '.') and self.isMatch(s[1:], p):#keep using *
                return True
            #not using the star anymore or use it 0 times
            return self.isMatch(s,p[2:])
        else: #no star following
            if len(s)>0 and (s[0] == p[0] or p[0] == '.'):
                return self.isMatch(s[1:],p[1:])
            return False
    """
    from functools import cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:

        @cache
        def dfs(i, j):                         # i indexes s, j indexes p
            # base cases
            if i == len(s) and j == len(p):
                return True
            if j == len(p):
                return False                   # s still has characters

            first_match = i < len(s) and (s[i] == p[j] or p[j] == '.')

            if j + 1 < len(p) and p[j + 1] == '*':
                # use the star once more
                if first_match and dfs(i + 1, j):
                    return True
                # use the star zero times
                return dfs(i, j + 2)
            else:                              # no star following
                if first_match:
                    return dfs(i + 1, j + 1)
                return False

        return dfs(0, 0)
        
