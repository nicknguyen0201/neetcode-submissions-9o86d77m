class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        x=2,n=3
        4=1 = 

        1 2. 3    4 
        2 4. 8


        res = 2
        power = 3
        while 1
            if 1=1
                res=2*4
            x=2*2=4 
            power>>=
        """
        res=1
        power=abs(n)
        while power:
            if power&1:
                res*=x
            x*=x
            power>>=1
        return res if n>0 else 1/res