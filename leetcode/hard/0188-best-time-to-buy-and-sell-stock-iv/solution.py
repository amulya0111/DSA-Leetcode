class Solution(object):

    def maxProfit(self, k, prices):
        n=len(prices)
        dp=[0]*(2*k+2)
        for i in range(n-1,-1,-1):
            for txn in range(2*k,-1,-1):
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
        # n = len(prices)
        # if n < 2 or k == 0:
        #     return 0
        # if k >= n // 2:
        #     profit = 0
        #     for i in range(1, n):
        #         if prices[i] > prices[i - 1]:
        #             profit += prices[i] - prices[i - 1]
        #     return profit
        # buy = [float('-inf')] * k
        # sell = [0] * k
        # for price in prices:
        #     for j in range(k):
        #         if j == 0:
        #             buy[j] = max(buy[j], -price)
        #         else:
        #             buy[j] = max(buy[j], sell[j - 1] - price)
        #         sell[j] = max(sell[j], buy[j] + price)

        # return sell[k - 1]