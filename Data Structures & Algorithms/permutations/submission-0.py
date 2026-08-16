class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        pick=[False]*len(nums)
        def BT(perm,picked):
            if len(perm)==len(nums):
                res.append(perm[:])
            for i, num in enumerate(nums):
                if not picked[i]:
                    picked[i]=True
                    perm.append(num)
                    BT(perm,picked)
                    perm.pop()
                    picked[i]=False
        BT([],pick)
        return res