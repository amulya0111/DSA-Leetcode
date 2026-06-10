class Solution(object):
    def firstUniqChar(self, s):
        """
        so we can have a dictionary to keep the count 
        we need to see which char's count is 1 
        problem is how to find index of the first char whose count is 1  
        """
        count = {}
        for ch in s:
            count[ch]=count.get(ch,0)+1
        for ch in range(len(s)):
            if count[s[ch]]==1:
                return ch
        return -1