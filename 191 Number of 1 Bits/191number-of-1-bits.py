class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        x=n
        count=0
        while x!=0:
            x=x&(x-1)
            count+=1
        return count
        