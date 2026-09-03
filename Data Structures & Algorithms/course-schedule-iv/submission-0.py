from functools import cache
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        """
        v: a,b,c
        c: u
        c is a prereq for v
        u is a prereq for c
        => u is a prereq for v
        """
        adj=defaultdict(list)
        for prereq,course in prerequisites:
            adj[course].append(prereq)
        @cache
        def dfs(target_u,v):#is u prereq of v
            if target_u==v:
                return True
            for prereq in adj[v]:
                if dfs(target_u,prereq):
                    return True
            return False
        res=[]
        for query in queries:
            res.append(dfs(query[0],query[1]))
        return res
            

