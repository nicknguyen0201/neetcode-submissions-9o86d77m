class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """

        AAA BBB CCC DDD

        A B C A B C A 

        idle=0
        process D
        idle= -2
        """
        freq=[0]*26
        for t in tasks:
            freq[ord(t)-ord('A')]+=1
        freq.sort()
        idle=(freq[25]-1)*n
        for i in range(24,-1,-1):
            idle-=min(freq[i],freq[25]-1)
        return max(idle, 0)+len(tasks)
