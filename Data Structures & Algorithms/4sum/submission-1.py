class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        nums.sort()
        def k_sum(start, k, quad):
            if k!=2:                                #[       ok x x x]
                for i in range(start,len(nums)-k+1):#[1,2,3,4,5,6,7,8] k=4
                    if i==start:
                        quad.append(nums[i])
                        k_sum(i+1,k-1,quad)
                        quad.pop()
                    else:
                        if nums[i]==nums[i-1]:
                            continue
                            #dedup
                        else:
                            quad.append(nums[i])#try different num for 1st pos in quad
                            k_sum(i+1,k-1,quad)
                            quad.pop()
            else:
                l,r=start,len(nums)-1
                t = target-sum(quad)#2sum new target
                
                while l<r:
                    if nums[l]+nums[r]>t:
                        r-=1
                    elif nums[l]+nums[r]<t:
                        l+=1
                    else:
                        
                        res.append(quad+[nums[l],nums[r]])
                        #might be more valid quad inside
                        l+=1
                        while l<r and nums[l]==nums[l-1]:
                            l+=1
        k_sum(0,4,[])
        return res