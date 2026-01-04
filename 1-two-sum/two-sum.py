class Solution(object):
    def twoSum(self, nums, target):
        n=len(nums)
        for i in range(n):
            for j in range(n):
                if nums[i]+nums[j]==target:
                    if i==j:
                        continue
                    return [i,j]

        
        