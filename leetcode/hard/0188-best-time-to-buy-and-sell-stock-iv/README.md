# Best Time to Buy and Sell Stock IV

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given an integer array `prices` where `prices[i]` is the price of a given stock on the `ith` day, and an integer `k`.

Find the maximum profit you can achieve. You may complete at most `k` transactions: i.e. you may buy at most `k` times and sell at most `k` times.

 **Note:**  You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Original
Python
 **Example 1:** 

```
Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

```

 **Example 2:** 

```
Input: k = 2, prices = [3,2,6,5,0,3]
Output: 7
Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

```

 

 **Constraints:** 

- 1 <= k <= 100
- 1 <= prices.length <= 1000
- 0 <= prices[i] <= 1000

## Solution

**Language:** Python  
**Runtime:** 78 ms (beats 18.84%)  
**Memory:** 12.1 MB (beats 94.48%)  
**Submitted:** 2026-11-13T12:19:41.074Z  

```py
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
```

---

[View on LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)