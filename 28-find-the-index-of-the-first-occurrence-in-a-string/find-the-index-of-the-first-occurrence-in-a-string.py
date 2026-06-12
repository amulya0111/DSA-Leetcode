class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        n=len(needle)
        if needle=="":
            return 0
        for i in range(len(haystack)-n+1): #9-3+1=7
            a=0
            if haystack[i]==needle[0]:
                a=1 
                for j in range(1,n): #1>3
                    if haystack[i+j]==needle[j]:
                        a=1
                    else:
                        a=0
                        break
                if a==1:
                    return i
        return -1
