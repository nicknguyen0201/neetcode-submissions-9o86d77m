class Solution:
    def integerBreak(self, n: int) -> int:
        """
        dp[5]=0
        {1:1
        2:2
        4:4
        3:3
        5:0}
        dfs(5)
            
            for i in range(1, 5):
                val=dfs(1)*dfs(4)

                    dfs(4)
                        dp[4]=4
                        for i in range(1,4)
                            val=dfs(1)*dfs(3)

                            dfs(3)=3
                                for i in range(1,3):
                                    val=dfs(1)*dfs(2)

                                    dfs(2)=2
                                        for i in range(1,2):
                                            val=dfs(1)*dfs(1)


        """
        dp={}
        dp[1]=1
        for num in range(2,n+1):
            dp[num]=num if n!=num else 0
            for i in range(1,num):
                dp[num]=max(dp[num],dp[num-i]*dp[i])
        return dp[n]


        """
        dry run
        dp  1 2 3 4
            1 2 3 4
        num=4
        res=0
        i=1
        dp[1]*dp[3]=3
        dp[2]dp[2]=4

        
        """
