from functools import cache
class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        """
        let dp[l][r] =  the score alice gets in range l, r
        dp[l+1][r] = the score alice gets when pick first element
        dp[l][r-1] = the score alice gets when pick last element
        when l==r we have 1 option =left

        because l+1 needed before l, so l has to go backward
        because r-1 needed before r, so r can go forward

        
        """
        n = len(piles)
        dp = [[0] * n for _ in range(n)]
        for l in range(n-1, -1,-1):
            for r in range(l,n):
                if l==r:
                    dp[l][r]=piles[l]
                    continue

                is_alice_turn =(r-l+1)%2==0

                right=piles[r] if is_alice_turn else 0
                left=piles[l] if is_alice_turn else 0
                dp[l][r]=max(dp[l+1][r]+left,dp[l][r-1]+right)
        return dp[0][n-1]>sum(piles)-dp[0][n-1]

