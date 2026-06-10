class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        lets make one dictionary to count letters in magazine 
        then traverse rN and check of count is available
        if yes , count-- and traverse, if not return false
        in the end return true
        """
        count={}
        for ch in magazine:
            count[ch]= count.get(ch,0)+1
        for ch in ransomNote:
            count[ch]= count.get(ch,0)-1
            if count[ch]==-1:
                return False
        return True
        