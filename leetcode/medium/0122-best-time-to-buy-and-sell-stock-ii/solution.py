class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp=[[-1]*2 for i in range(len(prices))]
        # # RECURSIVE:(BOTTOM UP)
        # def maxprofit(i,canbuy,prices):
        #     if i==len(prices):
        #         return 0
        #     if canbuy==1:
        #         # can buy
        #         # for i==0 there will be special cases 
                
        #         buy=-prices[i]+maxprofit(i+1,0,prices)                                  
        #         notbuy=0+maxprofit(i+1,1,prices)
        #         pick=buy
        #         notpick=notbuy
        #     else:
        #         # canbuy==0? > sell
        #         sell=prices[i]+maxprofit(i+1,1,prices)
        #         notsell=0+maxprofit(i+1,0,prices)
        #         pick=sell
        #         notpick=notsell
        #     return max(pick,notpick)
        # return maxprofit(0,1,prices)
        # # RECURSION+MEMOIZATION
        # # let buy=1 >can buy
        # def maxprofit(i,canbuy,prices,dp):
        #     if i==len(prices):
        #         return 0
        #     if dp[i][canbuy]!=-1:
        #         return dp[i][canbuy]
        #     if canbuy==1:
        #         # can buy
        #         # for i==0 there will be special cases 
                
        #         buy=-prices[i]+maxprofit(i+1,0,prices,dp)                                  
        #         notbuy=0+maxprofit(i+1,1,prices,dp)
        #         pick=buy
        #         notpick=notbuy
        #     else:
        #         # canbuy==0? > sell
        #         sell=prices[i]+maxprofit(i+1,1,prices,dp)
        #         notsell=0+maxprofit(i+1,0,prices,dp)
        #         pick=sell
        #         notpick=notsell
        #     dp[i][canbuy]=max(pick,notpick)
        #     return dp[i][canbuy]
        # return maxprofit(0,1,prices,dp)
        # # TABULATION:
        # n=len(prices)
        # dp=[[0]*(2) for i in range(n+1)]
        # # dp[n][0]=dp[n][1]=0
        # for i in range(len(prices)-1,-1,-1):
        #     for canbuy in range(2):
        #         if canbuy==1:
        #         # can buy
        #         # for i==0 there will be special cases 
                
        #             buy=-prices[i]+dp[i+1][0]                                 
        #             notbuy=0+dp[i+1][1]
        #             pick=buy
        #             notpick=notbuy
        #         else:
        #             # canbuy==0? > sell
        #             sell=prices[i]+dp[i+1][1]
        #             notsell=0+dp[i+1][0]
        #             pick=sell
        #             notpick=notsell
        #         dp[i][canbuy]=max(pick,notpick)
        # return dp[0][1]
        # SINGLE-ARRAY
        # dp=[0]*2
        # for i in range(len(prices)-1,-1,-1):
        #     for canbuy in range(2):
        #         if canbuy==1:
        #         # can buy
        #         # for i==0 there will be special cases 
                
        #             buy=-prices[i]+dp[0]                                 
        #             notbuy=0+dp[1]
        #             pick=buy
        #             notpick=notbuy
        #         else:
        #             # canbuy==0? > sell
        #             sell=prices[i]+dp[1]
        #             notsell=0+dp[0]
        #             pick=sell
        #             notpick=notsell
        #         dp[canbuy]=max(pick,notpick)
        # return dp[1]
        profit=0
        for i in range(1,len(prices)):
            profit += max(0, prices[i] - prices[i-1])
        return profit