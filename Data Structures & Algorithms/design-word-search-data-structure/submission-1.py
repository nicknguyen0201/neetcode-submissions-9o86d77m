class TrieNode:
    def __init__(self):
        self.mp=[None]*26
        self.eow=False
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()

    def addWord(self, word: str) -> None:
        curr=self.root
        for i,c in enumerate(word):
            
            if not curr.mp[ord(c)-ord('a')]:
                tmp=TrieNode()
                curr.mp[ord(c)-ord('a')]=tmp
                curr=tmp
            else:
                curr=curr.mp[ord(c)-ord('a')]
        curr.eow=True

            
    
    def search(self, word: str) -> bool:
        curr=self.root
        def dfs(curr,i):
            if i==len(word) and curr.eow:
                return True
            if len(word)==i:
                return False
            if word[i]=='.':
                for node in curr.mp:
                    if node:
                        flag=dfs(node,i+1)
                        if flag:
                            return True
            elif curr.mp[ord(word[i])-ord('a')]:
                curr=curr.mp[ord(word[i])-ord('a')]
                res=dfs(curr,i+1)
                return res
            else:
                return False
            return False

        return dfs(curr,0)

                
