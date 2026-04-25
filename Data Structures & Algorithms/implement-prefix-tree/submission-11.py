class TrieNode:
    def __init__(self):
        self.mp={}
        self.eow=False#end of word
class PrefixTree:

    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        curr=self.root
        for i, c in enumerate(word):
            
            if c in curr.mp:
                curr=curr.mp[c]
                if i==len(word)-1:
                    curr.eow=True
            else:
                curr.mp[c]=TrieNode()
                if i==len(word)-1:
                    curr.mp[c].eow=True
                curr=curr.mp[c]

    def search(self, word: str) -> bool:
        curr=self.root
        for i, c in enumerate(word):
            if c in curr.mp:
                curr=curr.mp[c]
                if i==len(word)-1 and curr.eow:
                    return True
            else:
                return False
        return False

    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for i, c in enumerate(prefix):
            if c in curr.mp:
                curr=curr.mp[c]
                if i==len(prefix)-1:
                    return True
            else:
                return False
        return False
        