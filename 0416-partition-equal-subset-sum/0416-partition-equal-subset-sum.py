class Solution(object):
    def canPartition(self, nums):
        k=sum(nums)
        n=len(nums)
        if k%2!=0:
            return False 
        k=k//2
        def checktarget(nums,k):
            # do same as subset sum target, 
            # initialize dp tabulation
            dp=[False]*(k+1) 
            dp[0]=True
            # if the value is less than target, the column will exist of the value == nums[0] is satisfied!
            if nums[0]<=k:
                dp[nums[0]]==True
            # why only nums[0]? as it will be the last element well check 
            # now comes the loop
            for i in range(n):
                for target in range(k,nums[i]-1,-1):
                    # not take condition , we just pick the previous value from upper column 
                    nottake=dp[target]
                    # first we will put take as false in case we cant have it(overload) to process it with not take 
                    take = False
                    if nums[i]<=target:
                        take=dp[target-nums[i]] #checking the remaining target if can be fulfilled or not from previous 
                    dp[target]=take or nottake
            return dp[k]
        return checktarget(nums,k) 
