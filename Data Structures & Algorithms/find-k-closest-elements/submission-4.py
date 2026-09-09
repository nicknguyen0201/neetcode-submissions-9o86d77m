import bisect
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        start=bisect.bisect_right(arr,x)

        """
        [2,4, 5, 8], k = 2, x = 6
         l       r
        start=3
        """
        r=start
        l=start-1
        for _ in range(k):
            if l<0:
                r+=1
            elif r>=len(arr):
                l-=1
            else:
                left, right=arr[l],arr[r]
                if abs(left-x)<abs(right-x):
                    l-=1
                elif abs(left-x)>abs(right-x):
                    r+=1
                else:
                    if left<right:
                        l-=1
                    else:
                        r+=1
        return arr[l+1:r]

