class TimeMap:

    def __init__(self):
        self.mp=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        self.mp[key].append((timestamp,value))
    def binsearch(self,arr,target):
        """
        10 20 30 t=25
        l. m   r
        """
        l,r=0,len(arr)-1
        while l<r:# we need to land on either target or anything immediately < than target
            m=(l+r)//2
            if arr[m][0]==target:
                return arr[m][1]
            elif arr[m][0]>target:
                r=m-1
            else:#arr<target
                l=m+1
        
        if arr[l][0]>target:
            if l-1<0:
                return ""
            return arr[l-1][1]

        return arr[l][1]
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mp:
            return ""
        return self.binsearch(self.mp[key],timestamp)
        