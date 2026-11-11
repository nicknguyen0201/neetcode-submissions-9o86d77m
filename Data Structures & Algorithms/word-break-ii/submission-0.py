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
            
            
        """
        res = []
        n = len(s)
        vocab = set(wordDict)
        def BT(start, path):
            if start == n:
                res.append(" ".join(path))
            for i in range(start, n):
                word = s[start:i+1]
                if word in wordDict:
                    path.append(word)
                    BT(i+1,path)
                    path.pop()
        BT(0,[])
        return res
