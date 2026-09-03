class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        
        adj={c:set() for w in words for c in w}
        for i in range(len(words)-1):
            w1,w2=words[i],words[i+1]
            size=min(len(w1),len(w2))
            if len(w1)>len(w2) and w1[:size]==w2[:size]:
                return ""
            for j in range(size):
                if w1[j]!=w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
            

        visited={}
        res=[]
        def dfs(c):
            if c in visited:
                return visited[c] #True means cycle, False means no cycle, no need to keep explorign
            visited[c]=True
            for nb in adj[c]:
                if dfs(nb):
                    return True
            visited[c]=False
            res.append(c)
            return False
        for c in adj.keys():
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)