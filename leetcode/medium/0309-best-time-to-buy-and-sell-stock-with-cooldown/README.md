# Best Time to Buy and Sell Stock with Cooldown

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

- After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).

 **Note:**  You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Original
Python
 **Example 1:** 

```
Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]

```

 **Example 2:** 

```
Input: prices = [1]
Output: 0

```

 

 **Constraints:** 

- 1 <= prices.length <= 5000
- 0 <= prices[i] <= 1000

## Solution

**Language:** Python  
**Runtime:** 4 ms (beats 30.59%)  
**Memory:** 12.7 MB (beats 37.14%)  
**Submitted:** 2026-11-14T14:46:32.551Z  

```py
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

                pick=-prices[i]+dp[i+1][0]
                notpick=0+dp[i+1][1]
                dp[i][1]=max(pick,notpick)
                
                pick=prices[i]+dp[i+2][1]
                notpick=0+dp[i+1][0]        
                dp[i][0]=max(pick,notpick)
        return dp[0][1]
```

---

[View on LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)