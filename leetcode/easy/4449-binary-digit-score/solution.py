class Solution(object):
    def calculateScore(self, a, b):
        s1=0
        s2=0
        while a:
            a=a&(a-1)
            s1+=1
        while b:
            b=b&(b-1)
            s2+=1
        if s1>=s2:
            return s1*s2
        if s1==0:
            return 0
        return s2//s1