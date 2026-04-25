class TrieNode:
    def __init__(self):
        self.mp={}
        self.eow=False
class PrefixTree:

    def __init__(self):
        self.root=TrieNode()

    def insert(self, word: str) -> None:
        curr=self.root
        for c in word:
            if c not in curr.mp:
                curr.mp[c]=TrieNode()
            curr=curr.mp[c]
        curr.eow=True

    def search(self, word: str) -> bool:
        curr=self.root
        for c in word:
            if c not in curr.mp:
                return False
            curr=curr.mp[c]
        return curr.eow
        

    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for c in prefix:
            if c not in curr.mp:
                return False
            curr=curr.mp[c]
        return True
        