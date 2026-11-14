class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        # # RECURSION
        # def profit(i,canbuy,prices):
        #     if i>=n:
        #         return 0
        #     if canbuy==1:
        #         pick=-prices[i]+profit(i+1,0,prices)
        #         notpick=0+profit(i+1,1,prices)
        #     else:
        #         pick=prices[i]+profit(i+2,1,prices)
        #         notpick=0+profit(i+1,0,prices)
        #     return max(pick,notpick)
        # return profit(0,1,prices)
        # TABULATION(ALONG WITH SINGLE)
        dp=[[0]*2 for i in range(n+1+1)]
        for i in range(n-1,-1,-1):
            for canbuy in range(2):
                if canbuy==1 :
                    pick=-prices[i]+dp[i+1][0]
                    notpick=0+dp[i+1][1]
                elif canbuy==0:
                    pick=prices[i]+dp[i+2][1]
                    notpick=0+dp[i+1][0]
        
                dp[i][canbuy]=max(pick,notpick)
        return dp[0][1]