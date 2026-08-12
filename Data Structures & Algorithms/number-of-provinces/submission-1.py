class DSU:
    def __init__(self,n):
        self.num_components=n
        self.parents=[i for i in range(n)]
        self.size=[1]*n

    def find(self,u):
        if self.parents[u]==u:
            return u
        self.parents[u] = self.find(self.parents[u])
        return self.parents[u]

    def union(self,u,v):
        pu=self.find(u)
        pv=self.find(v)
        if pu==pv:
            return 
        self.num_components-=1
        if self.size[pu]>self.size[pv]:
            self.size[pu]+=self.size[pv]
            self.parents[pv]=pu
        else:
            self.size[pv]+=self.size[pu]
            self.parents[pu]=pv
        
            
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        dsu=DSU(len(isConnected))
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j]:
                    dsu.union(i,j)
        return dsu.num_components
                    
