from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        set1=Counter(s)
        set2=Counter(t)
        return set1==set2