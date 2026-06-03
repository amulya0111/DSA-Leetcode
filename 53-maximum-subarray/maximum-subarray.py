class Solution(object):
    def maxSubArray(self, nums):
        max_sum = nums[0]
        sum=nums[0]
        for i in range(1,len(nums)):
            if nums[i]<sum+nums[i]:
                sum+=nums[i]
                max_sum=max(max_sum,sum)
            else:
                sum = nums[i]
                max_sum = max(nums[i],max_sum)
        return max_sum


        