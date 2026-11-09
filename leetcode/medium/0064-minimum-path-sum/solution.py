class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        # RECURSIVE:(BOTTOMUP)
        # def find(x,y,m,n):
        #     if x==m or y==n:
        #         return float('inf')
        #     if x==m-1 and y==n-1:
        #         return grid[x][y]
        #     right=grid[x][y]+find(x,y+1,m,n)
        #     down=grid[x][y]+find(x+1,y,m,n)
        #     return min(right,down)
        # return find(0,0,m,n)

        # TABULATION:(TOPDOWN)
        # dp=[[0]*n for i in range(m)]
        # for i in range(m-1,-1,-1):
        #     for j in range(n-1,-1,-1):
        #         if i==m-1 and j==n-1:
        #             dp[i][j]=grid[i][j]
        #             # it doesnt have right or down so continue
        #             continue
        #         right=grid[i][j]+(dp[i][j+1] if j+1<n else float('inf'))
        #         down=grid[i][j]+(dp[i+1][j]  if i+1<m else float('inf'))
        #         dp[i][j]=min(right,down)
        # return dp[0][0]

        # SINGLE-ARRAY:(TOP DOWN)
        dp=[0]*n
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i==m-1 and j==n-1:
                    dp[j]=grid[i][j]
                    continue
                right=grid[i][j]+(dp[j+1] if j+1 < n else float('inf'))
                down=grid[i][j]+(dp[j] if i+1 < m else float('inf'))
                dp[j]=min(right,down)
        return dp[0]