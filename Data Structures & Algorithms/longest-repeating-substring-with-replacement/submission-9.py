class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
            Understand:
            Plan:
            res 
            for every char in char set
                every char is potential to be replace to create a longest repeating 
                window 

                run a sliding window 
                count = 0
                for r in range (n):
                    if s[r]==c:
                        count+=1
                    if r-l+1 -count > k
                        if s[l]==c:
                            count-=1
                        l+=1
                    res = max

        """
        res =0
        char_set = set(s)
        n=len(s)
        for c in char_set:
            count = 0
            l=0
            for r in range (n):
                if s[r]==c:
                    count+=1
                if r-l+1 -count > k:
                    if s[l]==c:
                        count-=1
                    l+=1
                res = max(r-l+1,res)
        return res
