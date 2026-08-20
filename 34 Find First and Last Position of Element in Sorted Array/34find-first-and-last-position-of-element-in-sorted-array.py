class Solution(object):
    def searchRange(self, nums, target):
        if len(nums)==0:
            return [-1,-1]
        if len(nums)==1 and nums[0]==target:
            return [0,0]
        def findfirst(nums,target):
            firstidx=-1
            l=0
            h=len(nums)-1
            mid=(l+h)//2
            while l<h:
                if nums[mid]<target:
                    l=mid+1
                elif nums[mid]>target:
                    h=mid
                mid=(l+h)//2
                if nums[mid]==target:
                    firstidx=mid
                    h=mid
            return firstidx
        
        def findlast(nums,target):
            lastidx=-1
            l=0
            h=len(nums)-1
            mid=(l+h)//2
            while l<=h:
                if nums[mid]<target:
                    l=mid+1
                elif nums[mid]>target:
                    h=mid-1               
                elif nums[mid]==target:
                    lastidx=mid
                    l=mid+1
                mid=(l+h)//2
            return lastidx
        first=findfirst(nums,target)
        if first==-1:
            return [-1,-1]
        last=findlast(nums,target)
        return [first,last]
                
        