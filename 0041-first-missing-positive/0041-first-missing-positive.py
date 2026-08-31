class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sett=set()
        for i in range(len(nums)):
            sett.add(nums[i])
        for i in range(1,len(nums)+2):
            if i not in sett:
                return i
        return 1

