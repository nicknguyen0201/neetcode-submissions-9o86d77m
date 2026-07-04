from collections import Counter
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        plan use a freq map
        check if the current i can be expand to a point where
        all character in it subtract feq will become 0 if yes, split
        {
        x: 0
        y: 1
        z: 2
        b: 3
        i:1
        s:1
        l:1
        }
        ptr=4
        used={x,y}
        """
        freq=Counter(s)
        res=[]
        ptr=0
        used=set()
        flag=True
        for i, c in enumerate(s):
            #include in the substr
            if freq[c]-1>0:
                freq[c]-=1
                ptr+=1
                used.add(c)
            else:#freq[c]-1==0
                freq[c]-=1
                ptr+=1
                used.add(c)
                for ch in used:
                    if freq[ch]!=0:
                        flag=False
                        break
                
                if flag:
                    res.append(ptr)
                    ptr=0
                flag=True
        return res
                    
