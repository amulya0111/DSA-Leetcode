class Solution(object):
    def countValidSubstrings(self, s):
        res=left=0
        for i in range(len(s)):
            if i>=2 and s[i-2:i+1]=="abc":
                left=i-1
            res+=i-left+1
        return res