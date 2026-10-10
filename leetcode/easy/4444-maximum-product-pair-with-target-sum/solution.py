class Solution(object):
    def maxProductPair(self, nums, target):
        l=0        
        r=len(nums)-1
        result=[-1,-1]
        ans=float("-inf")
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    if ans<nums[i]*nums[j] and nums[i]!=nums[j]:
                        ans=nums[i]*nums[j]
                        result=[i,j] if nums[i]>nums[j] else [j,i]
                        
            
        return result