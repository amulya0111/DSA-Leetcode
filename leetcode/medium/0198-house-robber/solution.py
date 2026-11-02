class Solution(object):
    def rob(self, nums):
        if len(nums)<=2:
            return max(nums)
        dp=[0]*len(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1]) #As we can take farther value 0 for 2nd index 
        for i in range(2,len(nums)):
            pick=max(dp[i-2]+nums[i],nums[i])
            notpick=dp[i-1]
            dp[i]=max(pick,notpick)
        return dp[len(nums)-1]