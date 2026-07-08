class Solution:
    def isHappy(self, n: int) -> bool:
        
        def do_math(n):
            res=0
            while n!=0:
                res+=(n%10)**2
                n//=10
            return res
        seen=set()
        while n not in seen:
            seen.add(n)
            n= do_math(n)
            if n==1:
                return True
        return False
         
