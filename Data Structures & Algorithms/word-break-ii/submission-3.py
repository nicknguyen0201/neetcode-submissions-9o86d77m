from functools import cache
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """
           Input: s = "racecariscar", wordDict =                    ["racecar","race","car","is"]

Output: ["racecar is car","race car is car"]
                    i
            path = [ ]
            if start ==n:
                res.append(" ".join(path))
            for i in range(start, n):
                if s[:i+1] in wordDict:
                    path.append
                    BT(i+1)
                    path.pop
            
        run time
        at BT(0) for loop will make n call:
            BT(1), BT(2), BT(3), ...BT(N)
            each BT() child call will then make n-1 call
            n x n-1 x n-2 =n! chilren
            each BT() level we will do O(N) total splicing, and at at the each leaf we will do O(N) join operation
        n!n
        """

        res = []
        n = len(s)
        vocab = set(wordDict)
        path=[]
 
        def BT(start):
            if start == n:
                res.append(" ".join(path)) #O(N)
            for i in range(start, n): #O(N)
                word = s[start:i+1]#O(N)
                if word in vocab:
                    path.append(word)
                    BT(i+1)
                    path.pop()
        BT(0)
        return res
