class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def BT(open,close,tmp):
            if open==close==n:
                res.append("".join(tmp))
            if open<n:
                tmp.append('(')
                BT(open+1,close,tmp)
                tmp.pop()
            if close<open:
                tmp.append(')')
                BT(open,close+1,tmp)
                tmp.pop()
        BT(0,0,[])
        return res