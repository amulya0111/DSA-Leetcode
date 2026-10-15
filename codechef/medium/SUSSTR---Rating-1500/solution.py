# cook your dish here
from collections import deque
t=int(input())
for z in range(t):
    n=int(input())
    s=input()
    l=0
    r=n-1
    t=deque()
    oneseen= False
    i=0
    while l<=r:
        
        # first check alice 
        # to reduce she will obviously put zeros from left 
        if s[l]=='0':
            t.appendleft(s[l])
        elif s[l]=='1':
            t.append(s[l])
        l+=1 
        
        # now, check availability of bob's turn 
        # to increase he will obviously put ones from left 
        if l<=r:
            if s[r]=='1':
                t.appendleft(s[r])
            elif s[r]=='0':
                t.append(s[r])
            r-=1
    print("".join(t))