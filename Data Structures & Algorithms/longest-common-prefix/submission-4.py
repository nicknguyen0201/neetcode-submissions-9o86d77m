class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        res=strs[0]
        for i in range(len(strs)-1):
         
            j=0
            while j <min(len(strs[i]),len(strs[i+1])):
                if strs[i][j]!=strs[i+1][j]:
                   break
                j+=1
            res=res[:j]
                
        return res