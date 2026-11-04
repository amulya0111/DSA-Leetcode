class Solution:
    def calculateUniquePaths(self, rowCount, columnCount):
        # write your code here 
        # write your code here
        dp=[1]*columnCount
        for i in range(rowCount-2,-1,-1):
            for j in range(columnCount-2,-1,-1):
                dp[j]=dp[j]+dp[j+1]
        return dp[0]