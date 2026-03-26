class Solution(object):
    def fib(self, n):
        if n==0:
            return 0
        elif n==1:
            return 1
            #use self when you are using function of the class
        return self.fib(n-1)+self.fib(n-2)
        