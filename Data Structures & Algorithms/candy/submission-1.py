class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        high level overview
        I want to first assing minimun 1 candy for all
        when rating of i < i+1 
        we have to give 1 more candy to the i+1

        when i> i+1
        we have to make sure i has more candy than i+1
        can't sort because we lose positional info
        idea 1: linear scan (can't update element further away)
        4>3 3<5
        2 1 2

        7 6 5 4
        2 2 1 1
        """
        #first pass
        n=len(ratings)
        res = [1]*n
        for i in range(1,n):
            #if i larger than left nb, update
            if ratings[i] > ratings[i-1]: res[i] = res[i-1] + 1
        
        #2nd pass
        for i in range(n-2,-1,-1):
            #if i smaller than right nb, update between +1 or leave alone if the order alr correct
            if ratings[i] > ratings[i+1]: res[i] = max(res[i+1]+1,res[i])
        return sum(res)