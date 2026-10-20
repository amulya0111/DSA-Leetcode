def calculateSumOfSubarrayMinimums(inputArray):
    # write your code here 
    mod=10**9+7
    stack=[]
    res=0
    
    for i,x in enumerate(inputArray+[float('-inf')]): #  i/index and x/value at index 
        #inputArray + [float('-inf')]: We temporarily append negative infinity (-inf) to the end of the array. This acts as a "sentinel" value which forces the stack to pop and process all remaining elements at the end of the loop.
        while stack and inputArray[stack[-1]]>x:
            mid=stack.pop()
            left = mid - stack[-1] if stack else mid +1
            right = i-mid
            res+=inputArray[mid]*left* right
        stack.append(i)
    return res%mod 
    