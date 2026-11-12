# Best Time to Buy and Sell Stock III

![Difficulty](https://img.shields.io/badge/Difficulty-Hard-red)

## Problem

You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day.

Find the maximum profit you can achieve. You may complete  **at most two transactions**.

 **Note:**  You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Original
Python
 **Example 1:** 

```
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
```

 **Example 2:** 

```
Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.

```

 **Example 3:** 

```
Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

```

 

 **Constraints:** 

- 1 <= prices.length <= 105
- 0 <= prices[i] <= 105

## Solution

**Language:** Python  
**Runtime:** 226 ms (beats 51.12%)  
**Memory:** 20.6 MB (beats 92.44%)  
**Submitted:** 2026-11-12T18:16:04.364Z  

```py
class Solution(object):
    def maxProfit(self, prices):
        # # RECURSIVE:(BOTTOMUP)
        # def find(i,buy,cap):
        #     if cap==0 or i==len(prices):
        #         return 0
        #     if buy==1:
        #         buy=-prices[i]+find(i+1,0,cap)
        #         notbuy=0+find(i+1,1,cap)
        #         pick=buy
        #         notpick=notbuy
        #     else:
        #         sell=prices[i]+find(i+1,1,cap-1)
        #         notsell=0+find(i+1,0,cap)
        #         pick=sell
        #         notpick=notsell
        #     return max(pick,notpick)
        # return find(0,1,2)

        # TABULATION:(TOPDOWN)

            
        buy1 = float('-inf')
        sell1 = 0
        buy2 = float('-inf')
        sell2 = 0
        for price in prices:
            buy1 = max(buy1, -price)
            sell1 = max(sell1, buy1 + price)
            buy2 = max(buy2, sell1 - price)
            sell2 = max(sell2, buy2 + price)
        return sell2
```

---

[View on LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)