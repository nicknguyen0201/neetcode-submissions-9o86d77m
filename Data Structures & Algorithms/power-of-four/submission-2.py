class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """
        Highlevel over view
        1 *4 *4  = x
        recurse() that divide x by 4 repeatedly
        until base case x = 1, then return True

        if x=0 return false

        O(1) solutioin:
        n = 4^x = (2x2)^x = 2^x 2^x = 2^(2x)
        16 = 2^(2 . x=2)
        binary rep
        00000100 ->x = 1, n= 4
        00010000 ->x = 2, n= 16
        01000000 ->x = 3, n= 64
   
        if n == 1: return True
        if n == 0: return False
        return self.isPowerOfFour(n//4)
        """
        return n>0 and math.log(n,4) % 1 ==0
