class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        a a b
        0 1 2    3
        """
        res=[]
        def isPalindrome(s):
            return s==s[::-1]
        def dfs(i,lst):
            if i==len(s):
                res.append(lst[:])
                return 
            for j in range(i,len(s)):
                if isPalindrome(s[i:j+1]):
                    lst.append(s[i:j+1])
                    dfs(j+1,lst)
                    lst.pop()
        dfs(0,[])
        return res
