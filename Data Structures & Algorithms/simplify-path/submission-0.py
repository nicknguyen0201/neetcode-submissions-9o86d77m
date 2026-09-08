class Solution:
    def simplifyPath(self, path: str) -> str:
        s=[]
        lst=path.split('/')
        for name in lst:
            if name =="..":
                if s:
                    s.pop()
            elif name=='.' or name =="":
                continue
            else:
                s.append(name)
        return "/"+"/".join(s)


                