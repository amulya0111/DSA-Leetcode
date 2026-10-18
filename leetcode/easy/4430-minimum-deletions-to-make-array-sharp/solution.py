class Solution(object):
    def minDeletions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        ans=0
        for i in range(n-1,0,-1):
            if nums[i]^nums[i-1]==0:
                ans+=1
        return ans         