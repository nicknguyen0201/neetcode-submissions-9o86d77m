class TimeMap:

    def __init__(self):
        self.mp=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        self.mp[key].append((timestamp,value))
    def binsearch(self,arr,target):
        """
        10 20 30 t=25
        l. m   r

        1 3 5 7 9 t=4
          lr m
        """
        l,r=0,len(arr)-1
        res=''
        while l<=r:# we need to land on either target or anything immediately < than target
            m=(l+r)//2
            if arr[m][0]<=target:
                res=arr[m][1]
                l=m+1
            else:
                r=m-1
        return res

        return arr[l][1]
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp:
            return ""
        return self.binsearch(self.mp[key],timestamp)
        