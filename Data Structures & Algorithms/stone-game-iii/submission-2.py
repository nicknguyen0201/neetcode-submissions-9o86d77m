from functools import cache
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        """
        stoneValue=[2,4,3,1,2,3,1]

        """
        @cache
        def dfs(i, alice):
            if i>=len(stoneValue):
                return 0
            res= -float('inf') if alice else float('inf')
            score=0
            for j in range (i,i+3):
                if j>=len(stoneValue):
                    break
                if alice:
                    score+=stoneValue[j]
                    res=max(score+dfs(j+1,not alice),res)

                else:
                    score-=stoneValue[j]
                    res=min(score+dfs(j+1,not alice),res)
            return res
        alice_res=dfs(0,True)
        if alice_res==0:
            return 'Tie'
        return "Alice" if alice_res>0 else "Bob"
                
            