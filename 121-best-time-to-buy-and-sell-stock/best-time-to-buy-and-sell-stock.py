class Solution(object):
    def maxProfit(self, prices):
        # 7,1,5,3,6,4
        min_price=prices[0]
        max_profit=0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price= prices[i]
            else:
                profit = prices[i]-min_price
                if profit>max_profit:
                    max_profit=profit
        return max_profit