# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    height=list(map(int,input().split()))
    stack=[]
    water=0
    curr=0
    for i in range(n):
        if stack and height[i] >= height[stack[0]]:
            water = max(water, curr)
            curr = 0
            stack = []
        while stack and height[i]>=height[stack[-1]]:
            y=stack.pop()
            
            if not stack:
                break
            
            h=min(height[i],height[stack[-1]])-height[y]
            w=i-stack[-1]-1
            curr+=h*w
        stack.append(i)
    water=max(water,curr)
    print(water)