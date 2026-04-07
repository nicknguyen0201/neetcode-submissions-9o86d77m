class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        #
        l,res,window,satis=0,0,0,0
        #right ptr
        for r in range (len(customers)):
            if grumpy[r]:#if book store owner grumpy, accumulate
                window+=customers[r]
            else:
                satis+=customers[r]
            
            if r-l+1 > minutes:#if we accumulate more than minutes 
                if grumpy[l]:
                    window-=customers[l] #shrink from left but remove from window
                l+=1
            res=max(res,window)
        return res+satis