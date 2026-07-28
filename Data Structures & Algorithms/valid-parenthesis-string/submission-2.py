class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        ()(
        leftmin=-2
        leftmax=0
        """
        lmax,lmin=0,0
        for c in s:
            if c=='*':
                lmax+=1
                lmin-=1
            elif c=='(':
                lmax+=1
                lmin+=1
            else:
                lmax-=1
                lmin-=1
            if lmax<0:
                return False
            elif lmin<0:
                lmin=0
        return lmin==0