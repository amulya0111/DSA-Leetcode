class Solution(object):
    def containsDuplicate(self, nums):
        y = set(nums)
        if len(y)!=len(nums):
            return True
        return False
        