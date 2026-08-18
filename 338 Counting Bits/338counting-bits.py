class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # make and empty array of zeros
        ans = [0] * (n + 1)
        # now to find the bits , add right shift of it and add 1 if number was odd, 
        # right shift may only either remove odd part or nothing from even , we wont need to find it out 
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
            # 0= 0+0=0
            # 1= 0+1=1
            # 2= ans(2>>1=1)+0=1
            # 3= ans(3>>1=1)+1=2
            # 4= ans(4>>1=2)+0=1+0=1
            

        return ans