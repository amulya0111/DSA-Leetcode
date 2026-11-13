class Solution(object):
    def maxProfit(self, prices):
        # # RECURSIVE:(BOTTOMUP)
        # def find(i,buy,cap):
        #     if cap==0 or i==len(prices):
        #         return 0
        #     if buy==1:
        #         buy=-prices[i]+find(i+1,0,cap)
        #         notbuy=0+find(i+1,1,cap)
        #         pick=buy
        #         notpick=notbuy
        #     else:
        #         sell=prices[i]+find(i+1,1,cap-1)
        #         notsell=0+find(i+1,0,cap)
        #         pick=sell
        #         notpick=notsell
        #     return max(pick,notpick)
        # return find(0,1,2)

        # TABULATION:(TOPDOWN)
        n=len(prices)
        dp=[[[0]*3 for i in range(2)] for j in range(n+1)]
        for i in range(n-1,-1,-1):
            for canbuy in range(2):
                for cap in range(1,3):
                    if canbuy==1:
                        buy=-prices[i]+dp[i+1][0][cap]
                        notbuy=0+dp[i+1][1][cap]
                        pick=buy
                        notpick=notbuy
                    else:
                        sell=prices[i]+dp[i+1][1][cap-1]
                        notsell=0+dp[i+1][0][cap]
                        pick=sell
                        notpick=notsell
                    dp[i][canbuy][cap]=max(pick,notpick)
        return dp[0][1][2]
                
            
        # buy1 = float('-inf')
        # sell1 = 0
        # buy2 = float('-inf')
        # sell2 = 0
        # for price in prices:
        #     buy1 = max(buy1, -price)
        #     sell1 = max(sell1, buy1 + price)
        #     buy2 = max(buy2, sell1 - price)
        #     sell2 = max(sell2, buy2 + price)
        # return sell2