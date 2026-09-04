class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if not nums:
            return True
        total=sum(nums)
        if total%k!=0:
            return False
        target=total//k
        used=[False]*len(nums)
        
        def BT(i,k,subset_sum):
            if k==0:
                return True
            if subset_sum==target:
                return BT(0,k-1,0)
            for j in range(i,len(nums)):
                if used[j]:
                    continue
                if nums[j]+subset_sum>target:
                    continue
                used[j]=True
                if BT(j+1,k,subset_sum+nums[j]):
                    return True
                used[j]=False

            return False
        return BT(0,k,0)
