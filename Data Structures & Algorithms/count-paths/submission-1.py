import math
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        1 1 1 1 1 1
        1 2 3 4 5 6 
        1 3 6 10 15 21

        """
        
        return math.comb(m+n-2,n-1)