def fib(n):
    #Write your code here
    if n==1:
        return 0
    if n==2:
        return 1
    n= fib(n-1)+fib(n-2)
    return n
n = int(input())
print(fib(n))