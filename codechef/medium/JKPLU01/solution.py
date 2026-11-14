def calculateMaxProfit(stockPrices: list[int], transactionFee: int) -> int:
    n=len(stockPrices)
    dp=[0]*2
    for i in range(n-1,-1,-1):
        dp[1]=max(-stockPrices[i]+dp[0],0+dp[1])
        dp[0]=max(stockPrices[i]+dp[1]-transactionFee,0+dp[0])
    return dp[1]