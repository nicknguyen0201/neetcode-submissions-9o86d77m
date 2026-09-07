class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # 222 11 33 //3=2
        """
        2:1
        1:
        3:
        """
        freq=defaultdict(int)
        for num in nums:
            freq[num]+=1
            if len(freq)<3:
                continue
            newfreq=defaultdict(int)
            for n,cnt in freq.items():
                if cnt>1:
                    newfreq[n]=cnt-1
            freq=newfreq
        res=[]
        for num in freq.keys():
            if nums.count(num)>len(nums)//3:
                res.append(num)
        return res
                