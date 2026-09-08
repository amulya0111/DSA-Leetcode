class Solution(object):
    def countCommas(self, n):
        if n<1000:
            return 0
        else:
            # 1000,100000
            return n-999