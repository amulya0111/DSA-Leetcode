class Solution(object):
    def maxSubarraySumCircular(self, nums):
        currmax=currmin=maxsum=minsum=total=nums[0]
        for i in range(1,len(nums)):
            currmax=max(nums[i],currmax+nums[i])
            maxsum=max(currmax,maxsum)

            currmin=min(nums[i],currmin+nums[i])
            minsum=min(minsum,currmin)

            total+=nums[i]
        if maxsum < 0:
            return maxsum
        return max(maxsum,total-minsum)

        