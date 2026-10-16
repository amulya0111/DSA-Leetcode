# cook your dish here
from collections import deque
t=int(input())
for _ in range(t):
    n,k = map(int,input().split())
    arr=deque(list(map(int,input().split())))
    dq = deque()
    ans = []
    
    for i in range(n):
        # Remove indices that are outside the current window of size k
        if dq and dq[0] <= i - k:
            dq.popleft()
            
        # Remove smaller elements from the back as they are useless
        while dq and arr[dq[-1]] <= arr[i]:
            dq.pop()
            
        # Add current element index
        dq.append(i)
        
        # The window has reached size k, record the maximum (front of deque)
        if i >= k - 1:
            ans.append(str(arr[dq[0]]))
            
    print(" ".join(ans))
