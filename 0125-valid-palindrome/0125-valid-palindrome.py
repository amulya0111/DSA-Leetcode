class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        l=0
        r=len(s)-1
        while l<r:
            while not s[l].isalnum():
                if l==len(s)-1:
                    return True
                l+=1
            while not s[r].isalnum() and r>=0:
                r-=1
            if s[l].lower()!=s[r].lower():
                return False
            l+=1
            r-=1
        return True