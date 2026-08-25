class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """
        res=["JFK"]
        tickets.sort()
        mp=defaultdict(list)
        for src,dst in tickets:
            mp[src].append(dst)
        
        def dfs(src):
            if len(res)==len(tickets)+1: # each ticket use once
            #we also start at jfk hence +1
                return True
            for i,dst in enumerate(list(mp[src])):
                res.append(dst)
                mp[src].pop(i)
                tmp = dfs(dst)
                if tmp:
                    return True
                mp[src].insert(i,dst)
                res.pop()
            return False

        dfs("JFK")    
        return res
        """
        
        mp=defaultdict(list)
        tickets.sort()
        for src, dst in tickets[::-1]:
            mp[src].append(dst)

        res = []
        def dfs(src):
            while mp[src]:
                dst=mp[src].pop()
                dfs(dst)
            
            res.append(src)
            

        dfs("JFK")
        return res[::-1]