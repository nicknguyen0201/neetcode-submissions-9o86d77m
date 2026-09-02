class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort(reverse = True)
        adj=defaultdict(list)
        for src,dst in tickets:
            adj[src].append(dst)
        res=[]
        def dfs(airport):
            while adj[airport]: 
                nb=adj[airport].pop()
                dfs(nb)
            res.append(airport)
                
        dfs("JFK")
        return res[::-1]
        """

        adj{
        jfk:,
        hou:
        sea:
        }
        res = jfk, hou, jfk, sea,jfk
        """