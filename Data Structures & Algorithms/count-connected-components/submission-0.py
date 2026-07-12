class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #adj 
        mp=defaultdict(list)
        for a,b in edges:
            mp[a].append(b)
            mp[b].append(a)
        seen=set()
        def dfs(i):
            if i in seen:
                return 
            seen.add(i)
            for neighbor in mp[i]:
                if neighbor not in seen:
                    dfs(neighbor)
        res=0
        for i in range(n):
            if i not in seen:
                dfs(i)
                res+=1
        return res
        