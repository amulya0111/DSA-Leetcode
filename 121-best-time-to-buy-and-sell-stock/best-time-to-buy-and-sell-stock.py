class Solution(object):
    def maxProfit(self, prices):
        # 7,1,5,3,6,4
        min_price=prices[0]
        max_profit=0
        for i in range(len(prices)):
            min_price=min(min_price,prices[i])
            # if prices[i] < min_price:
            #     min_price= prices[i]
            # else:
            profit = prices[i]-min_price
            max_profit=max(max_profit,profit)
        return max_profit