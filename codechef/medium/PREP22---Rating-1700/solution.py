def largestRectangleArea(N: int, A: list[int]) -> int:
    stack=[]
    area=0
    for i in range(N):
        while stack and A[i]<A[stack[-1]]:
            y=stack.pop()
            h=A[y]
            if stack:
                w=i-stack[-1]-1
            else:
                w=i
            area=max(area,h*w)
        stack.append(i)
        
    while stack:
        y=stack.pop()
        h=A[y]
        if stack:
            w=N-stack[-1]-1
        else:
            w=N 
        area=max(area,h*w)
    return area 