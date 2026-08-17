class TrieNode:
    def __init__(self):
        self.mp={}
        self.index=-1
        self.references=0

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        directions=[(-1,0),(0,1),(1,0),(0,-1)]
        def valid(r,c):
            return r>=0 and c>=0 and r<len(board) and c<len(board[r]) and board[r][c]!='*'
        def dfs(r,c,root):
            if not valid(r,c):
                return 0
            found=0
            
            
            tmp=board[r][c]
            board[r][c]='*'
            child=root.mp.get(tmp)
            if not child:
                board[r][c]=tmp     
                return 0
            if child.index!=-1:
                res.append(words[child.index])
                child.index=-1
                found+=1
            
            for dr,dc in directions:
                nr,nc=dr+r,dc+c
                found+=dfs(nr,nc,child)
            child.references-=found
            board[r][c]=tmp
            if child.references==0:
                del root.mp[tmp]
            return found

        def add(root,word,i):
            curr=root
            for c in word:
                if c not in curr.mp:
                    curr.mp[c]=TrieNode()
                curr=curr.mp[c]
                curr.references+=1
            curr.index=i

        root=TrieNode()
        for i,word in enumerate(words):
            add(root,word,i)
        res=[]
        for r in range(len(board)):
            for c in range(len(board[r])):
                curr=root
                curr.references -=dfs(r,c,curr)
        return res
