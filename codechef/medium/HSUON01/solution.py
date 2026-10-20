def findNextGreaterElement(subsetNumbers, fullNumbers):
    dic={}
    stack=[]
    n=len(fullNumbers)
    for i in range(n-1,-1,-1):
        while stack and stack[-1]<=fullNumbers[i]:
            stack.pop()
        dic[fullNumbers[i]]=stack[-1] if stack else -1
        stack.append(fullNumbers[i])
    ans=[]
    for x in subsetNumbers:
        ans.append(dic[x])
    return ans
        
        
       