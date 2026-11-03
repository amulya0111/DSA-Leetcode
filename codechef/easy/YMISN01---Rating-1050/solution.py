class Solution:
    def calculateWaysToClimb(self, totalSteps: int) -> int:
        # write your code here 
        n=totalSteps
        if n==0 or n==1:
            return 1
        dp=[-1]*(totalSteps+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,totalSteps+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[-1]
            