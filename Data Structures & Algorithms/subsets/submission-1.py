class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        back tracking
        each level you decide keep or skip and element
        result = []

        def BT(i,path):
            if i= n:
                res.append(path
                return
            
            #skip
            BT(i+1,path)
            #take
            path.append
            BT(i+1)
            path.pop
        res = [[],[1],[2,3]]
        1 2 3
        i=0
        [1,2,3]


        """
        result = []

        def BT(i,path):
            if i == len(nums):
                result.append(path[:])
                return
            #skip
            BT(i+1,path)
            #take
            path.append(nums[i])
            BT(i+1,path)
            path.pop()
        BT(0,[])
        return result