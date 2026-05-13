class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        understnad:
        pick a chain of number that sum up to sum
        can use the same number many time
        can't have 2 chains that are the same
        P:
        decision to break
        for loop
        at each number, you can include this number, means add it to the sum and recurse on the resrt
        not include this number and go to next number

        """
        res=[]
        n=len(nums)
        def BT(start, sum, path):

            if sum==target:
                res.append(path[:])
                return 
            if sum>target:
                return
            if start>=n:
                return
            
            
            num=nums[start]
            path.append(num)
            BT(start, sum+num,path)
            path.pop()
            BT(start+1, sum, path)

        BT(0,0,[])
        return res