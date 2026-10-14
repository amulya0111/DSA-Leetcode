def findNextGreaterElements(numbers):
    stack=[]
    n=len(numbers)
    ans=[-1]*n
    for i in range(0,n):
        while stack and numbers[stack[-1]]<=numbers[i]:
            idx=stack.pop()
            ans[idx]=numbers[stack[-1]] if stack else -1
        stack.append(i)
    for i in range(n-1,-1,-1):\
        while stack and numbers[stack[-1]]<=numbers[i]:
            idx=stack.pop()
        if ans[i]==-1:
            ans[i]=numbers[stack[-1]] if stack else -1
        
    return ans
        