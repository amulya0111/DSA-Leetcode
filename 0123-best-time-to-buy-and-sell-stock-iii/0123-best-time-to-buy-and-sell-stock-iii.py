class Solution(object):
    def maxProfit(self, prices):
        n=len(prices)

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

        # # TABULATION:(TOPDOWN)
        # n=len(prices)
        # dp=[[[0]*3 for i in range(2)] for j in range(n+1)]
        # for i in range(n-1,-1,-1):
        #     for canbuy in range(2):
        #         for cap in range(1,3):
        #             if canbuy==1:
        #                 buy=-prices[i]+dp[i+1][0][cap]
        #                 notbuy=0+dp[i+1][1][cap]
        #                 pick=buy
        #                 notpick=notbuy
        #             else:
        #                 sell=prices[i]+dp[i+1][1][cap-1]
        #                 notsell=0+dp[i+1][0][cap]
        #                 pick=sell
        #                 notpick=notsell
        #             dp[i][canbuy][cap]=max(pick,notpick)
        # return dp[0][1][2]
        # # STRIVER OPTIMIZED CODE:
        n=len(prices)
        # dp=[[-1]*4 for i in range(n)]
        # def find(i,txn,dp):

        #     if i==n or txn==4:
        #         return 0
        #     if dp[i][txn]!=-1:
        #         return dp[i][txn]  
        #     if txn%2==0:
        #         # buy
        #         pick=-prices[i]+find(i+1,txn+1,dp)
        #         notpick=0+find(i+1,txn,dp)
        #     else:
        #         # sell
        #         pick=prices[i]+find(i+1,txn+1,dp)
        #         notpick=0+find(i+1,txn,dp)
        #     dp[i][txn]=max(pick,notpick)
        #     return dp[i][txn]
        # return find(0,0,dp)
        # # TABULATE:
        # dp=[[0]*5 for i in range(n+1)]
        # for i in range(n-1,-1,-1):
        #     for txn in range(3,-1,-1):
        #         if txn%2==0:
        #         # buy
        #             pick=-prices[i]+dp[i+1][txn+1]
        #             notpick=0+dp[i+1][txn]
        #         else:
        #             # sell
        #             pick=prices[i]+dp[i+1][txn+1]
        #             notpick=0+dp[i+1][txn]
        #         dp[i][txn]=max(pick,notpick)
        # return dp[0][0]
        # OPTIMIZE MORE!
        dp=[0]*5
        for i in range(n-1,-1,-1):
            for txn in range(3,-1,-1):
                if txn%2==0:
                # buy
                    pick=-prices[i]+dp[txn+1]
                    notpick=0+dp[txn]
                else:
                    # sell
                    pick=prices[i]+dp[txn+1]
                    notpick=0+dp[txn]
                dp[txn]=max(pick,notpick)
        return dp[0]
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