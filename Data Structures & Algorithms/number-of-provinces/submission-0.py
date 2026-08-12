class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:   
        visited=[False]*len(isConnected)
        res=0
        def dfs(node):
           
            visited[node]=True
            for nb in range(len(isConnected)):
                if isConnected[node][nb] and visited[nb]==False:
                    dfs(nb)
        for i in range(len(isConnected)):
            if not visited[i]:
                dfs(i)
                res+=1
        return res

            