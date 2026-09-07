class Solution(object):
    def minimumDeletions(self, nums):
        if len(nums)==1:
            return 1
        maxi=max(nums)
        mini=min(nums)
        n=len(nums)
        delete=0
        for i in range(len(nums)):
            if nums[i]==maxi:
                max_i=i
            if nums[i]==mini:
                min_i=i
        left = min(min_i, max_i)
        right = max(min_i, max_i)

        return min(
            right + 1,              
            n - left,               
            left + 1 + n - right    
        )