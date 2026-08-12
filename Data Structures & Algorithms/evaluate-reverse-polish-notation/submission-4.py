class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for c in tokens:
            if c not in "+-*/":
                stack.append(int(c))
            elif c=='+':
                x=stack.pop()
                y=stack.pop()
                stack.append(y+x)
            elif c=='-':
                x=stack.pop()
                y=stack.pop()
                stack.append(y-x)
            elif c=='*':
                x=stack.pop()
                y=stack.pop()
                stack.append(y*x)
            elif c=='/':
                x=stack.pop()
                y=stack.pop()
                stack.append(int(y/x))
        return stack.pop()
