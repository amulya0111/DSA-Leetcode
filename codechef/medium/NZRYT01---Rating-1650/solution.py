def calculate_max_profit(stockPrices):
    # buy1=buy2=-float('inf')
    # sell1=sell2=0
    # for Price in stockPrices:
    #     b1=buy1
    #     b2=buy2
    #     s1=sell1
    #     s2=sell2
    #     buy1=max(buy1,-Price)
    #     sell1=max(sell1,buy1+Price)
    #     buy2=max(buy2,sell1-Price)
    #     sell2=max(sell2,buy2+Price)
    # return sell2
    # # 
    n=len(stockPrices)
    dp=[0]*(5)
    for i in range(n-1,-1,-1):
        for txn in range(3,-1,-1):
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