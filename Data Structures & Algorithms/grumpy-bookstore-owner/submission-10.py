class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        """
        customers = [1,0,1,2,1,1,7,5],
           grumpy = [0,1,0,1,0,1,0,1],
                     1 0 1 0 1 1 7 5
                                3 mins

        U: return the max numbers of customers happy
        Find max consecutive minutes that maximize customers' satisfaciton
        use sliding window

        find the window size minutes that maximize customer satisfaction

        total satisfaction =  all - grumpy
        miximized satisfaction = 
        keep a max sum to measure how the maximize impact
                   0 1.    4
        customers=[1,2,3,4,5]
        grumpy=.  [1,0,1,0,1]
        minutes=2
        satis = 15 - 9 = 6


        """
        satisfaction = sum(customers)-sum( x*y for x,y in zip(customers,grumpy))
        max_satisfaction = 0
        n=len(customers)


        for i in range(n-minutes+1):#[0->n-minutes-1] [0-3)
            
            end=i+ minutes #2
            tmp=0#4
            for j in range(i, end):#[0, 2)
                if grumpy[j]==1:
                    tmp+=customers[j]
            max_satisfaction=max(max_satisfaction, tmp)
        return satisfaction+max_satisfaction



        
