class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        understand:
        generate subset
         plan:
        pick a number to be in the subset
        not picking that number to be in the subset
        do not use a number again 
        use 1
        [1] []
        [1, 2] [1] [2] []
        [1,2,3] [1,2] [1,3] [1] [2,3] [3]
        """
        n=len(nums)
        if not nums:
            return []
        def BT(start, path):
            if n==start:
                res.append(path[:])
                return
            
            path.append(nums[start])
            BT(start+1,path)
            path.pop()
            BT(start+1, path)
            
        res=[]
        BT(0,[])
        return res
