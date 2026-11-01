class Solution(object):
    def minMergedInteger(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def countdigits(n):
            x=n
            sum=0
            while x>0:
                x=x//10
                sum+=1
            return sum
        maxnum=float('inf')
        for i in range(1,len(nums)):
            if i%2==0:
                continue 
            newnum=nums[i-1]*(10**countdigits(nums[i]))+nums[i]
            maxnum=min(maxnum,newnum)
        return maxnum