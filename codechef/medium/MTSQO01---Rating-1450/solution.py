def calculateMaxRobAmount(houseMoneyList):
    # write your code here 
    nums=houseMoneyList
    if len(nums)<=3:
        return max(nums)
    def robbery(nums):
        dp=[0]*len(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,len(nums)):
            dp[i]=max(dp[i-2]+nums[i],dp[i-1])
        return dp[-1]
    dp1=robbery(nums[1:])
    dp2=robbery(nums[:-1])
    return max(dp1,dp2)