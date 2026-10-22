# cook your dish here
from collections import deque
t=int(input())
for _ in range(t):
    n=int(input())
    a=deque(list(map(int,input().split())))
    stack=[]
    b=[]
    need=1
    for i in range(len(a)):
        stack.append(a.popleft())
        while stack and stack[-1]==need:
            b.append(stack.pop())
            need+=1
    if need==n+1:
        print("YES")
    else:
        print("NO")
        