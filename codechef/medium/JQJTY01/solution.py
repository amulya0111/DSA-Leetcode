def calculateSumOfSubarrayMinimums(inputArray):
    # write your code here 
    mod=10**9+7
    stack=[]
    res=0
    
    for i,x in enumerate(inputArray+[float('-inf')]):
        while stack and inputArray[stack[-1]]>x:
            mid=stack.pop()
            left = mid - stack[-1] if stack else mid +1
            right = i-mid
            res+=inputArray[mid]*left* right
        stack.append(i)
    return res%mod 
    