class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n=len(prices)
        dp=[0]*2
        for i in range(n-1,-1,-1):
            dp[1]=max(-prices[i]+dp[0],0+dp[1])
            dp[0]=max(prices[i]+dp[1]-fee,0+dp[0])
        return dp[1]

        