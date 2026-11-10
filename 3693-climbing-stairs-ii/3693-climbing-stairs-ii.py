class Solution(object):
    def climbStairs(self, n, costs):
        
        dp=[0]*(n+1)

        for i in range(n-1,-1,-1):
            ans=float('inf')

            for step in range(1,4):
                if i+step<=n:
                    jump=costs[i+step-1]+step**2
                    ans=min(ans,jump+dp[i+step])

            dp[i]=ans

        return dp[0]