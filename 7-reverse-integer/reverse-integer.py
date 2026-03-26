class Solution(object):
    def reverse(self, x):
        # Handle sign
        sign = -1 if x < 0 else 1
        # Reverse using string slicing
        rev = int(str(abs(x))[::-1]) * sign
        # Check 32-bit range
        if -2**31 <= rev <= 2**31 - 1:
            return rev
        return 0