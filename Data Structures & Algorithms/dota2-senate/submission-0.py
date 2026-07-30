from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        """

        XXXDDDDD

        after round 1, remain
        X D
        after round 2
        x wins
        """
        r=deque()
        d=deque()
        n=len(senate)
        for i,senator in enumerate(senate):
            if senator=='R':
                r.append(i)
            else:
                d.append(i)
        while r and d:
            r_turn=r.popleft()
            d_turn=d.popleft()
            if r_turn < d_turn:
                r.append(r_turn+n)
            else:
                d.append(d_turn+n)
        return "Radiant" if r else "Dire"