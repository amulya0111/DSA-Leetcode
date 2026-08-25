class Solution(object):
    def lengthOfLastWord(self, s):
        s=reversed(s)
        count=0
        for char in s:
            if count==0 and char==" ":
                continue
            elif char.isalpha():
                count+=1
            elif char==" ":
                break

        return count
        