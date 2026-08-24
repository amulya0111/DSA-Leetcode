class Solution(object):
    def mySqrt(self, x):
        if x==0 or x==1:
            return x
        l=0
        r=x
        # [0 1 2 3 4 5 6 7 8] 
        while l<=r:
            mid=(l+r)//2 
            sq = mid*mid 
            if sq==x:
                return mid
            elif sq<x: 
                l=mid+1 
            else: 
                r=mid-1 
        return r
        