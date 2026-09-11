class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        """

        this is basically if you can make up a 
        subset target 4 times
        target=sum(nums)//4
        each matchstick, you 
        """
        total=sum(matchsticks)
        if total%4:
            return False
        target=total//4
        buckets=[0,0,0,0]
        matchsticks.sort(reverse=True)
        def dfs(i):
            if i==len(matchsticks):
                return True
            for j in range(4):
                if matchsticks[i]+buckets[j]<=target:#prune
                    buckets[j]+=matchsticks[i]
                    if dfs(i+1):
                        return True
                    buckets[j]-=matchsticks[i]
                if buckets[j]==0: #early exit
                    break
            return False
        return dfs(0)

            
