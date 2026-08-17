class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n==1:
            return True
        
        def dfs(node):
            visited.add(node)
            for nb in adj[node]:
                if nb not in visited:
                    dfs(nb)
            
        indeg = [0]*n
        adj=defaultdict(list)
        for u,v in edges:
            indeg[u]+=1
            indeg[v]+=1
            adj[u].append(v)
            adj[v].append(u)

        visited=set()
        dfs(0)
        if len(visited)!=n:#can't reach all node
            return False

        q=deque()
        len_q=0
        for i,num in enumerate(indeg):
            if num==1:
                q.append(i)
                len_q+=1
        
        while q:
            node = q.popleft()
            for nb in adj[node]:
                indeg[nb]-=1
                if indeg[nb]==1:
                    q.append(nb)
                    len_q+=1
        return len_q==n
        """
    3-  0 - 1 - 4
        |
        2

    0-1
    2-3
        """
        