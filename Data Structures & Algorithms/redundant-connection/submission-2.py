class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        I can do MST
        or just dfs and whenever we run into a visited node, return the edge to that node
        """
        adj=defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        seen=set()
        cycle_start=-1
        cycle_nodes=set()
        
        def dfs(node, parent):
            nonlocal cycle_start

            if node in seen:
                cycle_start=node
                return True
            
            seen.add(node)
            for nb in adj[node]:
                if nb!=parent:
                    if dfs(nb,node):
                        
                        if cycle_start!=-1:
                            cycle_nodes.add(node)
                        if node==cycle_start:
                            cycle_start=-1
                        return True
            return False
        dfs(edges[0][0],-1)
        for u,v in reversed(edges):
            if u in seen and v in cycle_nodes:
                return [u,v]
        return [-1,-1]

