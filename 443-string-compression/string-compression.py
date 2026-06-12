class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        l = 0
        i = 0
        while i < len(chars):
            ch = chars[i]
            count = 0
            while i < len(chars) and chars[i] == ch:
                count += 1
                i += 1
            chars[l] = ch
            l += 1
            if count > 1:
                for c in str(count):
                    chars[l] = c
                    l += 1

        return l