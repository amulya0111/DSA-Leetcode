class Solution:
    def calculateMinFallingPathSum(self, matrix):
        # write your code here
        m=len(matrix)
        n=len(matrix[0])
        dp=[0]*n
        for i in range(m-1,-1,-1):
            prev=dp[:]
            for j in range(n-1,-1,-1):
                if i==m-1:
                    dp[j]=matrix[i][j]
                    continue
                down=matrix[i][j] + prev[j]
                dialeft=matrix[i][j] + (prev[j-1] if j-1>=0 else float('inf'))
                diaright=matrix[i][j] + (prev[j+1] if j+1<m else float('inf'))
                dp[j]=min(down,dialeft,diaright)
        return min(dp)