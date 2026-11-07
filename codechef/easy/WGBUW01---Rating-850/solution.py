def calculateMaxProfit(stockPrices):
    l=0
    maxprofit=0
    if len(stockPrices)==1:
        return 0
    n=len(stockPrices)
    for r in range(1,n):
        if stockPrices[r]<=stockPrices[l]:
            l=r
        else:
            maxprofit=max(maxprofit,stockPrices[r]-stockPrices[l])
    return maxprofit 