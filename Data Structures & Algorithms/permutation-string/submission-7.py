class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Plan:
        2 freq mp size 26
        sliding window of size s1
       
        check repeatedly

        """
        if len(s1)>len(s2):
            return False
        
        mp1=[0]*26
        mp2=[0]*26
        for c in s1:
            mp1[ord(c)-ord('a')]+=1
        for i in range(len(s1)):
            c=s2[i]
            mp2[ord(c)-ord('a')]+=1
        if mp2==mp1:
            return True
        l=0
        for r in range(len(s1),len(s2)):
            c=s2[r]
            mp2[ord(c)-ord('a')]+=1
            mp2[ord(s2[l])-ord('a')]-=1
            l+=1
            if mp1==mp2:
                return True
        return False
