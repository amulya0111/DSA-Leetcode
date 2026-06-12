class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = s.split()
        for i in range(len(arr)):
            arr[i] = arr[i][::-1]
        return " ".join(arr)