class Solution(object):
    def countCommas(self, n):
        if n<1000:
            return 0
        if n<10**5:
            return n-999
        x=n
        l=0

        while n>0:
            l+=1
            n//=10
        else:
            i=l-1 #pow
            summ=0
            currx=x
            while i-3>=0:
                largest=i//3
                summ+= currx-(10**(i-(i%3)))+1
                i-=3
        return summ

            