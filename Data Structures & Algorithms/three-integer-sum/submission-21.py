class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        sort the arr
        then treat each number as an potential k
        do 2 ptr to find i and j such that  
        """
        nums.sort()
        n=len(nums)
        res=[]
        for k, kval in enumerate(nums):
            if kval>0:
                break
            if k>0 and nums[k]==nums[k-1]:
                continue
            l,r =k+1,n-1
            while l<r:
                if nums[l]+nums[r] +kval ==0:
                    res.append([nums[l],nums[r],kval])
                    r-=1
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                elif nums[l]+nums[r] +kval > 0:
                    r-=1
                else:
                    l+=1

        return res