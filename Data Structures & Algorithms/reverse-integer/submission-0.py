class Solution:
    def reverse(self, x: int) -> int:
        max_val=2**31-1
        min_val=-2**31
        res=0
        while x:
            digit=int(math.fmod(x,10))
            
            if res*10 > max_val or res*10+digit>max_val:
                return 0
            elif res*10<min_val or res*10+digit<min_val:
                return 0
            else:
                res=res*10+digit
            x=int(x/10)
        return res
