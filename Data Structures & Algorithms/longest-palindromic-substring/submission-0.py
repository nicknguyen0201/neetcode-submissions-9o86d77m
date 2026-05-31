class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=0
        longest_str=''
        n=len(s)
        for i in range(n):

            l,r = i,i
            tmp_max=0
            while l>=0 and r<n and s[l]==s[r]:
                tmp_max = r-l+1
                r+=1
                l-=1
            if res<tmp_max:
                res=tmp_max
                longest_str=s[l+1:r]
            l,r = i,i+1
            tmp_max=0
            while l>=0 and r<n and s[l]==s[r]:
                tmp_max = r-l+1
                r+=1
                l-=1
            if res<tmp_max:
                res=tmp_max
                longest_str=s[l+1:r]
        return longest_str

