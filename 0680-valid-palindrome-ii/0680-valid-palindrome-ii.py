class Solution(object):
    def isPalindrome(self, s,l,r):
        """
        :type s: str
        :rtype: bool
        """
        while l<r:
            while l<r and not s[l].isalnum():
                l+=1
            while l<r and not s[r].isalnum() and r>=0:
                r-=1
            if s[l].lower()!=s[r].lower():
                return False
            l+=1
            r-=1
        return True
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l=0
        r=len(s)-1
        while l<r:
            if s[l]==s[r]:
                l+=1
                r-=1
            else:
                return (self.isPalindrome(s,l+1,r) or self.isPalindrome(s,l,r-1))
        return True 