class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums)==1:
            return 1
        l=0
        k=1
        for r in range(1,len(nums)):
            if nums[l]!=nums[r]:
                l+=1
                nums[l]=nums[r]
                k+=1
        return k