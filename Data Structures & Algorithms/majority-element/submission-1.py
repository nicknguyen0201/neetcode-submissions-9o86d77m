class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq=defaultdict(int)
        for num in nums:
            freq[num]+=1
            if len(freq)>1:
                new_freq=defaultdict(int)
                for key,val in freq.items():
                    if val==1:
                        continue
                    else:
                        new_freq[key]=val-1
                freq=new_freq
        res= [key for key,val in freq.items()]#only run once
        return res[0]
