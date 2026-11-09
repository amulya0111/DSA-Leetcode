def canPartitionEqualSubset(numbers):
    total=sum(numbers)
    if total%2!=0:
        return False
    target=total//2
    n=len(numbers)
    dp=[False]*(target+1)
    dp[0]=True
    for i in range(n):
        for j in range(target,numbers[i]-1,-1):
            dp[j]= dp[j] or dp[j-numbers[i]]
    return dp[target]
