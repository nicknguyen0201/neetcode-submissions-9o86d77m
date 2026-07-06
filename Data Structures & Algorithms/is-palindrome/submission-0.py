class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        edge cases

        """
        l,r=0,len(s)-1
        s=s.lower()
        while l<r:
            if not s[l].isalnum():
                l+=1
            elif not s[r].isalnum():
                r-=1
            else:
                if s[r]!=s[l]:
                    return False
                r-=1
                l+=1
        return True
        