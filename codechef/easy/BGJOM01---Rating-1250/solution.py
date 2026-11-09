class Solution:
    def calculateMinimumPathSum(self, grid):
        # write your code here 
        m=len(grid)
        n=len(grid[0])
        dp=[0]*n
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i==m-1 and j==n-1:
                    dp[j]=grid[i][j]
                    continue
                right=grid[i][j] + (dp[j+1] if j+1<n else float('inf'))
                down=grid[i][j] + (dp[j] if i+1<m else float('inf'))
                dp[j]=min(right,down)
        return dp[0]