class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        maintain a adjacency list
        start at the entry has no prerequisite
        if we can go thru all, we return 
        map[ course 0 - n-1]-> list of its prereq
        we dfs every element of num courses

        we maintain 2 set
        visited: use when I am done visiting
        and cycle: use while I am visiting the node

        visited help us don't need to do a comprehensive O(V+E) dfs for
        every node

        """
        output=[]
        adlist = { c:[] for c in range(numCourses)}
        for course,prereq in prerequisites:
            adlist[course].append(prereq)
        
        visited, cycle=set(),set()
        def dfs(course):
            if course in cycle:
                return False #we have seen this course during our dfs
            if course in visited:
                return True #this course is reachable
            
            # dfs my own prereq
            cycle.add(course)
            for prereq in adlist[course]:
                if dfs(prereq)==False:
                    return False
            cycle.remove(course)
            visited.add(course)
            output.append(course)
            return True

        for course in range(numCourses):
            if dfs(course)==False:
                return []
        return output


