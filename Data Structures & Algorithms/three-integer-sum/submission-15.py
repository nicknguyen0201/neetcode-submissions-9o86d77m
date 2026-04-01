from collections import Counter
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        res=[]
        for i in range(n):
            numk=nums[i]
            if numk>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r = i+1, n-1
            while l<r:
                if nums[l]+nums[r]+numk==0:
                    res.append([nums[l],nums[r],nums[i]])
                    r-=1
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                elif nums[l]+nums[r]+numk>0:
                    r-=1
                else:
                    l+=1
            
        return res