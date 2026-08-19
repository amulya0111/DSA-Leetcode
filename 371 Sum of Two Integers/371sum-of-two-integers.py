class Solution(object):
    def getSum(self, a, b):
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF

        a &= MASK
        b &= MASK

        while b:
            a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK

        if a > MAX_INT:
            a = ~(a ^ MASK)

        return a