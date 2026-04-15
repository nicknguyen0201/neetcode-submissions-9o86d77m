class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        output=[]
        for i, num in enumerate(nums):
            if num>0:
                break
            if i>0 and nums[i-1]==num:
                continue
            l=i+1
            r=n-1
            while l<r:
                if num+nums[l]+nums[r]<0:
                    l+=1
                elif num +nums[l]+nums[r]>0:
                    r-=1
                else:
                    output.append([num, nums[l],nums[r]])
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    l+=1
                    r-=1

        return output

