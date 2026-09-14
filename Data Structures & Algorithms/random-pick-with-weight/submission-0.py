class Solution:

    def __init__(self, w: List[int]):
        self.total=sum(w)
        self.prefix=[1]*len(w)
        self.prefix[0]=w[0]
        for i in range(1,len(w)):
            self.prefix[i]=self.prefix[i-1]+w[i]

    def pickIndex(self) -> int:
        target=self.total*random.random()
        l,r =0, len(self.prefix)-1
        while l<r:
            m=l+(r-l)//2
            if self.prefix[m]<target:
                l=m+1
            else:
                r=m
        return l

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()