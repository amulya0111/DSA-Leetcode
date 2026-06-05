class Solution(object):
    def findMin(self, nums):
        """
        how about we find median and compare 
        find minimum
        [4,5,6,7,0,1,2]
        we will find mid = 7/2=3
        compare with mid+1 and mid-1
        it might happen that we still are in left sorted array
        if we are still in left sorted , we know nums[0] is not the minimum,move right 
        """
        beg = 0
        end = (len(nums)-1)
        mid = (beg+end)//2
        n = len(nums)-1

        if nums[0] <= nums[n]:
            return nums[0]
        while beg<=end:
            if mid>0 and nums[mid]<nums[mid-1]:
                return nums[mid] 
            if nums[0]<=nums[mid]:
                beg = mid+1
                mid=(beg+end)//2
            elif nums[0]>nums[mid]:
                end=mid-1
                mid=(beg+end)//2
        return nums[beg]    

        