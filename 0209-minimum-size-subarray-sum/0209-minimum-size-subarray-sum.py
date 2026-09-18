class Solution(object):
    def minSubArrayLen(self, target, nums):
        ans=float('inf')
        l=0
        r=0
        curr=nums[l]
        if curr>=target:
            return 1
        while l<=r and r<=len(nums):            
            if curr<target:
                if r+1==len(nums):
                    break
                curr+=nums[r+1]
                r+=1
            else:
                while curr>=target:                      
                    ans=min(ans,r-l+1)    
                    curr-=nums[l]
                    l+=1
                       
                
        if ans == float('inf'):
            return 0
        return ans