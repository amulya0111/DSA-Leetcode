class Solution(object):
    def maxProductPair(self, nums, target):
        l=0        
        r=len(nums)-1
        result=[-1,-1]
        ans=float("-inf")
        while l<=r:
            s=nums[l]+nums[r]
            if s<target:
                l+=1
            elif s>target:
                r-=1
            else:
                if ans<(nums[l]*nums[r]):
                    result=[r,l]
                    ans=(nums[l]*nums[r])
                l+=1
                r-=1
            
        return result