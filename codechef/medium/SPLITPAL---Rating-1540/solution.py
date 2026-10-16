# cook your dish here
from collections import deque
t=int(input())
for z in range(t):
    n=int(input())
    arr=deque(list(map(int,input().split())))
    
    ans=0
    
    while len(arr)>1:
        
        x=arr.popleft()
        y=arr.pop()
        if x==y:
            continue
        else:
            ans +=1
            if x<y:
                arr.append(y-x)
            elif x>y:
                arr.appendleft(x-y)
    print(ans)
                