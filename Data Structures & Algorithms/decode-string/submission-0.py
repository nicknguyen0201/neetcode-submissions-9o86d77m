class Solution:
    def decodeString(self, s: str) -> str:
        self.i=0
        """
        "2[a3[b]]c"
        i=8
        dfs()
        c=[
        k=2
        res=2*abbb
            dfs()
            k=0
            res=a + 3*b
                dfs()
                res=''
                k=0
            


        """
        def dfs():
            k=0
            res=''
            while self.i<len(s):
                c=s[self.i]
                if c.isdigit():
                    k=k*10+int(c)
                    self.i+=1
                elif c=='[':
                    self.i+=1
                    res+= k*dfs()
                    k=0
                elif c==']':
                    self.i+=1
                    return res
                else:
                    res+=c
                    self.i+=1
            return res
        return dfs()
            