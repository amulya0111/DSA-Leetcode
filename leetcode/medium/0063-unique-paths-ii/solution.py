class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        # RECURSIVE:(BOTTOM UP)
        # def find(x,y,m,n,grid):
        #     if x==m-1 and y==m-1:
        #         return 1
        #     if x>m-1 or y>n-1 or grid[x][y]==1:
        #         return 0
        #     right=find(x,y+1,m,n,grid)
        #     down=find(x+1,y,m,n,grid)
        #     return right+down     
        # return find(0,0,m,n,obstacleGrid)

        # TABULATION:(TOP DOWN)
        if obstacleGrid[m-1][n-1]==1 or obstacleGrid[0][0]==1:
            return 0
        dp=[[0]*n for i in range(m)]
        dp[m-1][n-1]=1
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i==m-1 and j==n-1:
                    continue
                if obstacleGrid[i][j]==1:
                    dp[i][j]=0
                    continue 
                right=dp[i][j+1] if j+1 < n else 0
                down = dp[i+1][j] if i+1 < m else 0
                dp[i][j]=right+down
        return dp[0][0]           
