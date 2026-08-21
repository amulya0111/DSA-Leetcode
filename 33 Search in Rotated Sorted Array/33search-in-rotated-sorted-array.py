class Solution(object):
    def search(self, nums, target):
        """
        
        """
        r=len(nums)-1
        if r+1==0:
            return -1
        if r+1==1 and nums[r]==target:
            return 0
        l=0
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                return mid 
            # Left half is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            # Right half is sorted
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1
        