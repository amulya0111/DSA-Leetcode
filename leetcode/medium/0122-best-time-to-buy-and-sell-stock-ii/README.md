# Best Time to Buy and Sell Stock II

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

On each day, you may decide to buy and/or sell the stock. You can only hold  **at most one**  share of the stock at any time. However, you can sell and buy the stock multiple times on the  **same day**, ensuring you never hold more than one share of the stock.

Find and return  *the  **maximum**  profit you can achieve*.

 

Original
Python
 **Example 1:** 

```
Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.

```

 **Example 2:** 

```
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.

```

 **Example 3:** 

```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

```

 

 **Constraints:** 

- 1 <= prices.length <= 3 * 104
- 0 <= prices[i] <= 104

## Solution

**Language:** Python  
**Runtime:** 39 ms (beats 5.09%)  
**Memory:** 17 MB (beats 6.87%)  
**Submitted:** 2026-11-13T11:04:23.072Z  

```py
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
        dp=[0]*2
        for i in range(len(prices)-1,-1,-1):
            for canbuy in range(2):
                if canbuy==1:
                # can buy
                # for i==0 there will be special cases 
                
                    buy=-prices[i]+dp[0]                                 
                    notbuy=0+dp[1]
                    pick=buy
                    notpick=notbuy
                else:
                    # canbuy==0? > sell
                    sell=prices[i]+dp[1]
                    notsell=0+dp[0]
                    pick=sell
                    notpick=notsell
                dp[canbuy]=max(pick,notpick)
        return dp[1]
        # profit=0
        # for i in range(1,len(prices)):
        #     profit += max(0, prices[i] - prices[i-1])
        # return profit
```

---

[View on LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)