class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        res=l
        """
        weights=[1,2,3,4,5,6,7,8,9,10]
        10 .. 55
        mid=65/2=32
        2 ships <5 ships:
        l=10 r=31

        mid=20
        4 ships <=5 ships

        mid=15
        5 ship<= 5ships
        res=15
        l=10, r=14
        mid=12
        6>5
        l=13
        6>5
        l=14
        6>5
        l=15 stops
        """
        while l<r:
            mid=(l+r)//2
            #aasume mid is the max capactity, can we make it in d days
            cap=mid
            ship=1
            for w in weights:
                if cap-w>=0:
                    cap-=w
                else:
                    ship+=1
                    cap=mid
                    cap-=w
            if ship<=days:#we need to decrease cap to try to bring ship closer days
                res=mid
                r=mid
            else: #ship>days:  we need to increase cap to reduces ship needed
                l=mid+1
        return l

