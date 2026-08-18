class Solution(object):
    def findPeakElement(self, nums):
        l=0
        h=len(nums)-1
        while l<h:
            m=(l+h)//2
            if nums[m+1]>nums[m]:
                l=m+1
            else:
                h=m
        return l


        