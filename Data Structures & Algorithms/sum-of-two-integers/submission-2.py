class Solution:
    def getSum(self, a: int, b: int) -> int:
        """
        7+4
        0111
        0100
        

        carry = 0000
        a=1011
        b=0
        a= 0011& 1111(mask)=0011
        b=1000 & 1111=1000

        """
        max_int=0x7FFFFFFF
        mask=0xFFFFFFFF
        while b!=0:
            carry=(a&b)<<1
            a= (a^b)&mask
            b=carry&mask
        return a if a<max_int else ~(a^mask)
            