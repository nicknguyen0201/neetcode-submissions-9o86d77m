from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        P:
        freq dict t
        need and have variable
        res, and res len variables
        window freq dict
        right pointer go right

        when we have char in t, we increment window count
        when have==need 
        check res update res
        """
        t_mp = Counter(t)
        s_mp = Counter(t)
        need=0
        for key, val in s_mp.items():
            s_mp[key]=0
            need+=1
        
        l=0
        res=(-1,-1)
        res_len=float('infinity')
        have =0
        n=len(s)

        for r in range(n):
            c=s[r]
            if c in s_mp:
                s_mp[c]+=1
                if s_mp[c]==t_mp[c]:
                    have+=1
                while have==need:
                    new_len = r-l+1
                    if res_len>new_len:
                        res_len=new_len
                        res=(l,r)
                    if s[l] in s_mp:
                        s_mp[s[l]]-=1
                        if s_mp[s[l]]<t_mp[s[l]]:
                            have-=1
                    l+=1
        l,r=res
        if l==-1 and r==-1:
            return ""
        return s[l:r+1]
