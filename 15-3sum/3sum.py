class Solution(object):
    def threeSum(self, nums):
        #firstly , sort the list for better checking
        nums.sort()
        op=[]
        for i in range(len(nums)-2):
            # for duplicate values 
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target=-nums[i]
            left = i+1
            right = len(nums)-1
            while right > left:
                x=nums[right]+nums[left]
                if x > target:
                    right-=1
                elif x < target:
                    left+=1
                else:
                    y = [nums[i],nums[left],nums[right]]
                    op.append(y)
                    left+=1
                    right-=1
                    while left < right and nums[left]==nums[left-1]:
                        left+=1
                    while left <right and nums[right]==nums[right+1]:
                        right-=1
            
        return op