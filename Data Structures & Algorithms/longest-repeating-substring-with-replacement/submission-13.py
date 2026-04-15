class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Maintani a size k window
        inside the window we keep track of the largest repeating char
        have a counter to keep track of char
        Input: s = "AAABA BB", k = 1
        maxf=4
        max_len=4
        """
        window_mp=[0]*26
        #max char count inside the windwo
        maxf=0
        l=0
        n=len(s)
        max_len=0
        
        for r,c in enumerate(s):
            window_mp[ord(c)-ord('A')]+=1
            maxf=max([x for x in window_mp])
            
            # if window size - k replacement > curr max char count in window
            # 5 -2 > 2
            #shrink
            if r-l+1 - k >maxf:
                window_mp[ord(s[l])-ord('A')]-=1
                maxf=max([x for x in window_mp])
                l+=1
            max_len=max(max_len,r-l+1)
        return max_len


