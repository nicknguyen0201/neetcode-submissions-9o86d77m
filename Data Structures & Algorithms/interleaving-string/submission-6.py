class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1)+len(s2)!=len(s3):
            return False
        dp=[[False]*(len(s2)+1) for _ in range(len(s1)+1)]
        dp[len(s1)][len(s2)]=True
        for i in range(len(s1),-1,-1):
            for j in range(len(s2),-1,-1):
               
                if i<len(s1)and s1[i]==s3[i+j] and dp[i+1][j]:
                    dp[i][j]=True
                if j<len(s2) and s2[j]==s3[i+j] and dp[i][j+1]:
                    dp[i][j]=True
        return dp[0][0]
        """ 
       one wrong assumption I made is
       interleaving definition has to be exactly like how the problem example
        0 1 2 3 4 5 6 7 8 
        a a b b b b a a
       
                0   1   2   3   4
                b   b   b   b        
        0    a  T   F   F    F   F

        1    a  T   F   F    T   F

        2    a  T   T   T    T   T

        3    a  F   F   F    F   T i
                                
        4       F    F   F   F   T  -  can I make s3[i+j:] s2[j:] and s1[i:]

                            j
        
       """
