class Solution(object):
    def minFallingPathSum(self, matrix):
        m=len(matrix)
        n=len(matrix[0])
        # RECURSIVE:(BOTTOMUP)
        # def find(x,y,m,n):
        #     if x==m-1:
        #         return matrix[x][y]
        #     down=matrix[x][y]+find(x+1,y,m,n)
        #     dialeft=matrix[x][y]+(find(x+1,y-1,m,n) if y-1>=0 else float('inf'))
        #     diaright=matrix[x][y]+(find(x+1,y+1,m,n) if y+1<n else float('inf'))
        #     return min(down,dialeft,diaright)
        # return find(0,0,m,n)

        # TABULATION:(TOPDOWN)
        # dp=[[0]*n for _ in range(m)]
        # for i in range(m-1,-1,-1):
        #     for j in range(n-1,-1,-1):
        #         if i==m-1:
        #             dp[i][j]=matrix[i][j]
        #             continue
        #         down=matrix[i][j]+(dp[i+1][j] if i+1<m else float('inf'))
        #         dialeft=matrix[i][j]+(dp[i+1][j-1] if i+1<m and j-1>=0 else float('inf'))
        #         diaright=matrix[i][j]+(dp[i+1][j+1] if i+1<m and j+1<n else float('inf'))
        #         dp[i][j]=min(down,dialeft,diaright)
        # return min(dp[0][:])

        # SINGLE-ARRAY:(BOTTOMUP)
        dp=[0]*n
        for i in range(m-1,-1,-1):
            prev=dp[:]
            for j in range(n-1,-1,-1):                
                if i==m-1:
                    dp[j]=matrix[i][j]
                    continue
                down=matrix[i][j]+prev[j]
                dialeft=matrix[i][j]+(prev[j-1] if j-1>=0 else float('inf'))
                diaright=matrix[i][j]+(prev[j+1] if j+1<n else float('inf'))
                dp[j]=min(down,dialeft,diaright)
        return min(dp)
        # we use prev as like before we dont need right or down(in which only down should be previous)
        # prev helps us attain prev of dialeft and diaright as well (the right was of same column,dialeft and diaright are of prev columns only )