class Solution:
    
    def partition(self, s: str) -> List[List[str]]:
        """
        plan:
        inside each function, we decide to take the word or not take the char
        at each point, decide where to end

        a a b
        aa b
        a ab

        """
        def is_palindrome(word):
            return word==word[::-1]
        res=[]
        n=len(s)
        def BT(start,path):

            if start ==n:
                res.append(path[:])
                return

            for end in range(start, n):
                tmp = s[start:end+1]
                if is_palindrome(tmp):
                    path.append(tmp)
                    BT(end+1, path)
                    path.pop()
        BT(0,[])
        return res
