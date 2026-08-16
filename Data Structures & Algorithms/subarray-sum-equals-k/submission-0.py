class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """

        [1,1,1] k=2
        res=1
        run=1
        diff=-1
        {-1:1
        0:1
        1:1
        2:1


        }
      
        """
        prefix={0:1}
        running_sum=0
        res=0
        for num in nums:
            running_sum+=num
            diff=running_sum-k
            res+= prefix.get(diff,0)
            prefix[running_sum]=1+prefix.get(running_sum,0)
        return res
