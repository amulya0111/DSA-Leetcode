class Solution(object):
    def reverse(self, x):
        n=abs(x)
        rev=0
        while n>0:
            r=n%10
            rev=rev*10+r
            n=n/10
        if x<0:
            if (-2**31)<=rev<=(2**31-1):
                return -rev
            else:
                return 0
        else:
            if (-2**31)<=rev<=(2**31-1):
                return rev
            else:
                return 0
        
        