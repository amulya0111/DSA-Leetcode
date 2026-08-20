class Solution(object):
    def searchInsert(self, nums, target):
        l=0
        r=len(nums)-1
        if r+1==0:
            return -1
        if r==0 and nums[0]==target:
            return 0
        mid=(l+r)//2
        while l<r:                        
            if nums[mid]<target:
                l=mid+1
            elif nums[mid]>target:
                r=mid
            mid=(l+r)//2
            #we check the l=r situation at most once here 
            # which means if target not present , at last mid=l=r
            if nums[mid]==target:
                return mid
        if nums[mid]<target:
            return mid+1
        else:
            return mid
        