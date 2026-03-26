class Solution(object):
    def isPalindrome(self, x):
        rev=0
        n=x
        while n>0:
            r=n%10
            rev=rev*10+r
            n=n/10
        if rev==x:
            return True
        else:
            return False
        