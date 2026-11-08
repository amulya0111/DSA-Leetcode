class Solution:
    def countUniquePaths(self, grid):
        # write your code here
        m=len(grid)
        n=len(grid[0])
        if grid[0][0]==1 or grid[m-1][n-1]==1:
            return 0
        dp=[0]*n
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i==m-1 and j==n-1:
                    dp[n-1]=1
                    continue
                if grid[i][j]==1:
                    dp[j]=0
                    continue
                right=dp[j+1] if j+1<n else 0
                down=dp[j] if i+1<m else 0
                dp[j]=right+down
        return dp[0]