class Solution(object):
    def containsDuplicate(self, nums):
        y = set(nums)
        if len(y)!=len(nums):
            return True
        return False
        # sett = set()
        # for num in nums:
        #     if num in sett:
        #         return True
        #     sett.add(num)
        # return False