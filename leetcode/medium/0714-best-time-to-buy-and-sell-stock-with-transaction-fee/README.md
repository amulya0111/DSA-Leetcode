# Best Time to Buy and Sell Stock with Transaction Fee

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day, and an integer `fee` representing a transaction fee.

Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

 **Note:** 

- You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
- The transaction fee is only charged once for each stock purchase and sale.

 

Original
Python
 **Example 1:** 

```
Input: prices = [1,3,2,8,4,9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
- Buying at prices[0] = 1
- Selling at prices[3] = 8
- Buying at prices[4] = 4
- Selling at prices[5] = 9
The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.

```

 **Example 2:** 

```
Input: prices = [1,3,7,5,10,3], fee = 3
Output: 6

```

 

 **Constraints:** 

- 1 <= prices.length <= 5 * 104
- 1 <= prices[i] < 5 * 104
- 0 <= fee < 5 * 104

## Solution

**Language:** Python  
**Runtime:** 150 ms (beats 38.44%)  
**Memory:** 16.3 MB (beats 96.10%)  
**Submitted:** 2026-11-14T15:05:18.405Z  

```py
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

        
```

---

[View on LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)