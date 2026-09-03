from collections import deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [n-1]
        adj=defaultdict(list)
        indeg=defaultdict(int)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
            indeg[u]+=1
            indeg[v]+=1

        visited=set()
        q=deque()
        for node, neighbors in indeg.items():
            if neighbors==1:
                q.append(node)
                visited.add(node)
        
        while q:
            if n<=2:
                return list(q)
            for _ in range(len(q)):
                node=q.popleft()
                n-=1
                for nb in adj[node]:
                    indeg[nb]-=1
                    if nb not in visited and indeg[nb]==1:
                        q.append(nb)
                        visited.add(node)
        return list(q)