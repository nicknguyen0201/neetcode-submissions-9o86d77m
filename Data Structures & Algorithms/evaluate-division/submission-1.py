class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj=defaultdict(list)

        for i,[src,dst] in enumerate(equations):
            adj[src].append((dst,values[i]))
            adj[dst].append((src,1/values[i]))

        def dfs(src, dst, visited):
            if src not in adj or dst not in adj:
                return -1
            if src==dst:
                return 1
            visited.add(src)
            for nb,w in adj[src]:
                if nb not in visited:
                    res=dfs(nb,dst,visited)
                    if res!=-1:
                        return res*w

            return -1
        return [dfs(q[0],q[1],set()) for q in queries]

        