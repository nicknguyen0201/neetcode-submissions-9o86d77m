class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        for i in n
            at each i we can take or not take the num
            then we can keep backtrack from i to end with k-1
        """
        res=[]
        def BT(i,k,comb):
            if k==0:
                res.append(comb[:])
                return 
            if i==n+1:
                return
            
            comb.append(i)
            BT(i+1,k-1,comb)
            comb.pop()
            BT(i+1,k,comb)
        BT(1,k,[])
        return res