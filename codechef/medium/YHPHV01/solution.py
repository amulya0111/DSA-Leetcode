

def calculateMaxProfit(maxTransactions, stockPrices):
    n=len(stockPrices)
    dp=[0]*(2*maxTransactions+2)
    for i in range(n-1,-1,-1):
        for txn in range(2*maxTransactions-1,-1,-1):
            if txn%2==0:
            # buy
                pick=-stockPrices[i]+dp[txn+1]
                notpick=0+dp[txn]
            else:
                # sell
                pick=stockPrices[i]+dp[txn+1]
                notpick=0+dp[txn]
            dp[txn]=max(pick,notpick)
    return dp[0]