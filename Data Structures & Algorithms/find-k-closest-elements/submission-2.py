import bisect
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        start=bisect.bisect_right(arr,x)

        """
        [2,4, 5, 8], k = 2, x = 6
              l  r
        start=3
        """
        r=start
        l=start-1
        res=[]
        while k>0 and (r<len(arr) or l>=0):
            if l>=0 and r<len(arr):
                num=0
                if abs(arr[l]-x) < abs(arr[r]-x):
                    num=arr[l] 
                    l-=1
                elif abs(arr[l]-x) > abs(arr[r]-x):
                    num=arr[r]
                    r+=1
                else:
                    if arr[l]< arr[r]:
                        num=arr[l]  
                        l-=1
                    else:
                        num=arr[r]
                        r+=1
                res.append(num)
                
                
            elif l>=0:
                res.append(arr[l])
                l-=1
            else:
                res.append(arr[r])
                r+=1
            k-=1
        res.sort()
        return res

