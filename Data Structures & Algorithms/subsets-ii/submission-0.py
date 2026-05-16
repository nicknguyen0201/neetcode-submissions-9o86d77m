class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n=len(nums)
        res=[]
        def BT(start, path):
            if start>=n:
                res.append(path[:])
                return 
            path.append(nums[start])
            BT(start+1, path)
            path.pop()

            while start+1< n and nums[start]==nums[start+1]:
                start+=1
            BT(start+1,path)
            
        BT(0,[])
        return res