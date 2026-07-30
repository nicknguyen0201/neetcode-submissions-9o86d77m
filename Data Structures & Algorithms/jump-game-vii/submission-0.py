class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        if s[len(s)-1]=='1':
            return False
        dp=[False]*len(s)
        dp[0]=True
        cnt=0
        for i in range(len(s)):
            if i>=minJump and dp[i-minJump]:
                cnt+=1
            if i>maxJump and dp[i-maxJump-1]:
                cnt-=1
            if cnt>0 and s[i]=='0':
                dp[i]=True
        return dp[len(s)-1]