class Solution(object):
    def uniquePaths(self, m, n):
        # instead of pick and notpick , there will be right and down 
        dp=[1]*n
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                dp[j]=dp[j]+dp[j+1]
        return dp[0]

        # dp=[[1]*n for i in range(m)]
        # # for dp, change from bottom up to top down
        # for i in range(m-2,-1,-1):
        #     for j in range(n-2,-1,-1):
        #         dp[i][j]=dp[i][j+1]+dp[i+1][j]
        # return dp[0][0]


        # def countways(x,y,m,n):
        #     if x==m-1 and y==n-1:
        #         return 1
        #     elif x>=m or y>=n:
        #         return 0
        #     # right or down
        #     right = countways(x,y+1,m,n)
        #     down  = countways(x+1,y,m,n)
        #     return right + down
        # return countways(0,0,m,n)