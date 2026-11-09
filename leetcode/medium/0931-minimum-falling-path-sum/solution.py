class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m=len(matrix)
        n=len(matrix[0])
        # RECURSIVE:(BOTTOMUP)
        # def find(x,y,m,n):
        #     if x==m-1:
        #         return matrix[x][y]
        #     down=matrix[x][y]+find(x+1,y,m,n)
        #     dialeft=matrix[x][y]+(find(x+1,y-1,m,n) if y-1<0 else float('inf'))
        #     diaright=matrix[x][y]+(find(x+1,y+1,m,n) if y+1<n else float('inf'))
        #     return min(down,dialeft,diaright)
        # return find(0,0,m,n)

        # TABULATION:(TOPDOWN)
        dp=[[0]*n for _ in range(m)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i==m-1:
                    dp[i][j]=matrix[i][j]
                    continue
                down=matrix[i][j]+(dp[i+1][j] if i<m else float('inf'))
                dialeft=matrix[i][j]+(dp[i+1][j-1] if j-1>0 else float('inf'))
                diaright=matrix[i][j]+(dp[i+1][j+1] if j+1<n else float('inf'))
                dp[i][j]=min(down,dialeft,diaright)
        return dp[0][0]