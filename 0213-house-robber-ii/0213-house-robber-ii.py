class Solution(object):
    def rob(self, nums):
        if len(nums)<=2:
            return max(nums)
        def house(nums):
            dp=[0]*len(nums)
            dp[0]+=nums[0]
            dp[1]+=max(nums[0],nums[1])

            for i in range(2,len(nums)):
                dp[i]=max(dp[i-2]+nums[i],dp[i-1])
            return dp[-1]
        dp1=house(nums[:-1])
        dp2=house(nums[1:])
        return max(dp1,dp2)
