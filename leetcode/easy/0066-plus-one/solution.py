class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s=0
        carry=1
        for i in range(len(digits)-1,-1,-1):
            n=digits[i]+carry
            s=n%10
            carry=n//10
            digits[i]=s
        if carry>0:
            digits.insert(0,carry)
        return digits