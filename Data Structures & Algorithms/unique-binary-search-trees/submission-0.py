class Solution:
    def numTrees(self, n: int) -> int:
        """
        count=[0,1,2,0,0]
        count =3
            left=0 right=2
            left=1 right =1
            left=2 right =0
        """
        count=[0]*(n+1)
        count[0]=1
        count[1]=1
        for cnt in range(2,n+1):
            for root in range(cnt):
                left_subtree=root#0,1,2
                right_subtree=cnt-left_subtree-1#2,1,0
                count[cnt]+=count[left_subtree]*count[right_subtree]
        return count[n]
