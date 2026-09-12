class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        """
        make sure the thing %k
        also sort
        build a tree return True if you can make up to k in 1 branch
        """
        total=sum(nums)
        if total % k:
            return False
        target = total//k
        used=[False]*len(nums)
        nums.sort(reverse=True)
        def dfs(i,sum,remain):
            if sum==target:
                return dfs(0,0,remain-1)
            if remain==0:
                return True
            if sum > target:
                return False
            for j in range(i,len(nums)):
                if not used[j]:
                    used[j]=True
                    if dfs(j+1,sum+nums[j],remain):
                        return True
                    used[j]=False
                    if sum==0:#there is at lease 1 invalid element that > target
                        return False
            return False
        return dfs(0,0,k)


