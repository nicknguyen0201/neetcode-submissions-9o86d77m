class Solution:
    def isValid(self, s: str) -> bool:
        """
        stack keep tracks of (, {, [

        if see a closing bracket match the top stack:
            continue
        else return false

        check stack empty

         "([()]"
         st = [ (
        """
        mp={"(":")", 
            "{":"}",
            "[":"]"}
        stack=[]
        for c in s:
            
            if c in mp:#opeinging bracke
                stack.append(c)
            elif not stack: # stack has nothing to compare with incoming
                return False
            elif mp[stack.pop()] != c: #top stack opening not matching closing 
                return False
            else:
                continue #top stack match
        return len(stack)==0 #all open not closed entirely

                