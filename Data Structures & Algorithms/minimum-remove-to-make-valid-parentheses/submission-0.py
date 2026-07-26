class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]
        res=[]
        for i,c in enumerate(s):
            if c=='(':
                stack.append(i)
            elif c==')':
                if stack:
                    # we don't have ( for this )
                    stack.pop()
                else:
                    res.append('')
                    continue
            res.append(c)
        while stack:
            res[stack.pop()]=''
        return "".join(res)
