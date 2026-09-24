from functools import cache
class TrieNode:
    def __init__(self):
     
        self.children={}
        self.eow=False
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def add_word(self,word):
        curr=self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]=TrieNode()
            
            curr=curr.children[c]
        curr.eow=True

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        """
        neetscode
            i
        max(dfs(eetcode,1),dfs(scode,4)
            dfs(code,5),dfs(8))
        """
        trie=Trie()
        for word in dictionary:
            trie.add_word(word)
        

        @cache
        def dfs(i):
            if i==len(s):
                return 0
            res=1+dfs(i+1)
            curr=trie.root
            for j in range(i,len(s)):
                if s[j] not in curr.children:
                    break
                curr=curr.children[s[j]]
                if curr.eow:
                    res=min(res,dfs(j+1))
            return res
        return dfs(0)


        

        