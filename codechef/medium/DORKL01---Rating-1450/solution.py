def countCoinCombinations(targetAmount, coinDenominations):
    amount=targetAmount
    coins=coinDenominations
    n=len(coinDenominations)
    prev=[0]*(amount+1)
    prev[0]=1
    for i in range(n-1,-1,-1):
        dp=[0]*(amount+1)
        dp[0]=1
        for target in range(amount+1):
            pick=0
            if coins[i]<=target:
                pick=dp[target-coins[i]]
            notpick=prev[target]
            dp[target]=pick+notpick
        prev=dp[:]

    return prev[amount] 
    
