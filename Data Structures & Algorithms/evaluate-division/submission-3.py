class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        highlev overview

        a/b = 4
        b/c = 1

        a - b, edge w = 4, a to b and b to a has diff edge w, b-a = 1/4
        b - c, edge w = 1
        a/c = a/b *b/c  = 4*1 use the edges' weight product    

        ab / bc, edge w = 3.25
        ab is a variable name not a*b

        how to represent the maps
        req store edge w between  u and v
        also store edge w bt v and u
        {
            a: {b:1,c:2}
            b: {c:1/2, a:2}
        }
        do 1 dfs pass per query
        
        pseudo code
        
        """
        def dfs(src,dest,visited):
            if src in visited:
                return -1
            visited.add(src)
            neighbors_map = graph[src]
            #traverse
            #check if neighbor is dest base case
            if dest in neighbors_map:
                return neighbors_map[dest]

            for neighbor, value in neighbors_map.items():
                #keep searching
                if neighbor in visited:
                    continue
                
                candidate = dfs(neighbor,dest,visited)
                
                if candidate != -1:
                    return candidate * value
            return -1 #exhaused neighborhood

        graph = defaultdict(lambda: defaultdict(float))
        for (src, dest), value in zip(equations,values):
            graph[src][dest] = value
            graph[dest][src] = 1.0 / value
        
        res = []
        for src,dest in queries:
            if src in graph:
                res.append(dfs(src,dest,set()))
            else:
                res.append(-1.0)
        return res
