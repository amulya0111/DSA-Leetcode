class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # logic - if n&(n-1)==0 , as we can see the other lower digits will become 1 and the main bit will be 0
        # & will give 0 
        if n>0 and n&(n-1)==0:
            return True
        else:
            return False
