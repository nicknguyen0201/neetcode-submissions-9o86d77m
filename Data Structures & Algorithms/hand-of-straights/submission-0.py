class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        Plan:
        sort 
        build 4 group empty array
        traverse

        if repeating, put in new basket
        if not repeat, put into current basket that has number [i]-1

        """
        if len(hand)%groupSize !=0:
            return False
        num_group = len(hand)//groupSize
        hand.sort()
        mp=defaultdict(list)
        cnt=0
        for num in hand:
            for i in range(num_group):
                if len(mp[i])==groupSize:
                    continue
                if len(mp[i]) == 0 or mp[i][-1]==num-1:
                    mp[i].append(num)
                    #found a basket, move on
                    break
                 
        for i in range(num_group):
            if len(mp[i])!=groupSize:
                return False
        return True
      
