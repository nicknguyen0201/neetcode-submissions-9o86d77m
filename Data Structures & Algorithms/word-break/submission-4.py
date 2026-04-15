class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet=set(wordDict)
        n=len(s)
        memo={}
        def BT(start):
            if start==n:
                return True
            if start in memo:
                return memo[start]
            for r in range(start, n):
                if s[start:r+1] in wordSet:
                    res = BT(r+1)
                    if res:
                        memo[start]=True
                        return True
            memo[start]=False
            return False
        return BT(0)
        

                

        