

def calculateMaxProfit(stockPrices):
# TABULATION(ALONG WITH SINGLE)
    prices=stockPrices
    n=len(prices)
    dp=[[0]*2 for i in range(n+1+1)]
    for i in range(n-1,-1,-1):

            pick=-prices[i]+dp[i+1][0]
            notpick=0+dp[i+1][1]
            dp[i][1]=max(pick,notpick)
            
            pick=prices[i]+dp[i+2][1]
            notpick=0+dp[i+1][0]        
            dp[i][0]=max(pick,notpick)
    return dp[0][1]


