class Solution(object):

    def maxProfit(self, k, prices):
        n = len(prices)
        if n < 2 or k == 0:
            return 0
        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit
        buy = [float('-inf')] * k
        sell = [0] * k
        for price in prices:
            for j in range(k):
                if j == 0:
                    buy[j] = max(buy[j], -price)
                else:
                    buy[j] = max(buy[j], sell[j - 1] - price)
                sell[j] = max(sell[j], buy[j] + price)

        return sell[k - 1]