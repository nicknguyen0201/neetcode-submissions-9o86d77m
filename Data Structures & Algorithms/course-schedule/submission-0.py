from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        is this a DAG detection:
        I don't remember how to detect cycle
        we do dfs on every single node is 1 way

        build an adjacency list
        do dfs and remove edge of prereq if we can get the prereq
        """
        in_deg=[0]*numCourses
        adj=defaultdict(list)
        for dst, src in prerequisites:
            in_deg[dst]+=1
            #directed graph go from lower class to higher class
            adj[src].append(dst)
        q=deque()
        #store indeg=0
        finish =0
        for i, indeg in enumerate (in_deg):
            if indeg==0:
                finish+=1
                q.append(i)
   
        while q:
            course = q.popleft()
            for neighbor in adj[course]:
                if in_deg[neighbor]-1==0:
                    #take this course will cause this neighbor to become new course with 0 indeg
                    finish+=1
                    q.append(neighbor)
                in_deg[neighbor]-=1
        return finish==numCourses
                

                
                




