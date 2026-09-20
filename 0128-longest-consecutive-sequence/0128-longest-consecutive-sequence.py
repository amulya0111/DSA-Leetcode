class Solution(object):
    def longestConsecutive(self, nums):
        seen=set(nums)
        maxi=0
        for num in seen:
            if num-1 not in seen:
                curr=num
                length=1
                while curr+1 in seen:
                    length+=1
                    curr+=1
                maxi=max(length,maxi)
        return maxi


        