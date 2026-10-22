# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    stack=[]
    ans=[None]*n
    for i in range(n):
        while stack and stack[-1]>a[i]:
            stack.pop()
        ans[i]=stack[-1] if stack else -1
        stack.append(a[i])
    print(" ".join(map(str,ans)))
    