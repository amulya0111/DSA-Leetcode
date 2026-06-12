class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        index=0
        if s=="":
            return True
        for i in range(len(t)):
            if t[i]==s[index]:
                index+=1
            if index == len(s):
                return True
        return False