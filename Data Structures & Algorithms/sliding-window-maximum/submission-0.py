from heapq import heappush, heappop
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        if n<=k:
            return [max(nums)]
        h=[]
        res=[]
        for i in range(k):
            heappush(h,(-nums[i],i))
        res.append(-h[0][0])
        for i in range(k,n):
            heappush(h,(-nums[i],i))
            while h[0][1]<=i-k:
                heappop(h)
            res.append(-h[0][0])
        return res
        """
        [3,2,1,2] k =3
        """