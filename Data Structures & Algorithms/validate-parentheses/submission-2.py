class Solution:
    def isValid(self, s: str) -> bool:
        """
        stack
        open brackets: add to stack
        when close brackets, check the stack for the right bracket

        if not empty at the end
        mp={
        '(':')'
        ,'[':']'
        ,'{': '}'
        }
        stack=[]
        for c in s:
            if c in mp:
                stack.append(stack)
            else:
                #closing
                if not stack:
                    return False
                if mp[stack[-1]]!=c:
                    return False
                stack.pop()
        return True
        """
        
        mp={
        '(':')'
        ,'[':']'
        ,'{': '}'
        }
        stack=[]
        for c in s:
            if c in mp:
                stack.append(c)
            else:
                #closing
                if not stack:
                    return False
                if mp[stack[-1]]!=c:
                    return False
                stack.pop()
        return not stack 