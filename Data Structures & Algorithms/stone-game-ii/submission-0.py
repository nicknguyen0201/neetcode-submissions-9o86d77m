from functools import cache
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        """
        [3,1,2,5,7]
        alice 
        M=1
        X= 1, 2
            use x=1
            take 3 +dfs(bob turn,i=1,M=1) =7
            return 10
                    bob 
                    X=1,2
                    take 1 
                    return dfs( alice turn, i=2, M=1) =7

                            alice
                            X=1,2
                            take 2,5
                            7+ dfs(bob, i=2+2,M=2) =0

                                bob
                                x=2,4
                                take 7 
                                return dfs(alice turn, i=5,M=2)
                                        return 0


        """
        @cache
        def dfs(alice, i, M):
            if i>=len(piles):
                return 0
            total=0
            if alice==False:
                total=float('inf')
            take=0
            for X in range(1, M*2+1):
                if i-1+X >= len(piles):
                    break
                take+=piles[i-1+X]
                if alice:
                    total = max(total, take + dfs(not alice, i+X,max(X,M)))
                else:
                    total=min(total, dfs(not alice, i+X,max(X,M)))
            return total
        return dfs(True,0,1)