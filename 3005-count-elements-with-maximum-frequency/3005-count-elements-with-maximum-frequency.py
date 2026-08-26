class Solution(object):
    def maxFrequencyElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        freq={}
        for num in nums:
            freq[num]=freq.setdefault(num,0)+1
        maximum=max(freq.values())
        for key in freq:
            if freq[key]==maximum:
                count+=maximum
        return count