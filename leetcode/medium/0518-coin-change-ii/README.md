# Coin Change II

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return  *the number of combinations that make up that amount*. If that amount of money cannot be made up by any combination of the coins, return `0`.

You may assume that you have an infinite number of each kind of coin.

The  **final**  answer is  **guaranteed**  to fit into a signed  **32-bit**  integer.

 

Original
Python
 **Example 1:** 

```
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

```

 **Example 2:** 

```
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

```

 **Example 3:** 

```
Input: amount = 10, coins = [10]
Output: 1

```

 

 **Constraints:** 

- 1 <= coins.length <= 300
- 1 <= coins[i] <= 5000
- All the values of coins are unique.
- 0 <= amount <= 5000

## Solution

**Language:** Python  
**Runtime:** 488 ms (beats 31.61%)  
**Memory:** 12.6 MB (beats 82.05%)  
**Submitted:** 2026-11-16T05:15:09.943Z  

```py
class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        n=len(coins)
        # dp=[[-1]*(amount+1) for i in range(n)]
        # def count(i,target,coins,dp):
        #     if target==0:
        #         return 1
        #     if i==len(coins):
        #         return 0
        #     if coins[i]>target:
        #         return count(i+1,target,coins,dp)
        #     if dp[i][target]!=-1:
        #         return dp[i][target]
        #     pick=0+count(i,target-coins[i],coins,dp)
        #     notpick=0+count(i+1,target,coins,dp)
        #     return pick+notpick
        # return count(0,amount,coins,dp)

        # dp=[[0]*(amount+1) for i in range(n+1)]
        # for i in range(n+1):
        #     dp[i][0]=1
        # for i in range(n-1,-1,-1):
        #     for target in range(amount+1):
        #         pick=0
        #         if coins[i]<=target:
        #             pick=dp[i][target-coins[i]]
        #         notpick=dp[i+1][target]
        #         dp[i][target]=pick+notpick
        # return dp[0][amount]

        prev=[0]*(amount+1)
        prev[0]=1
        for i in range(n-1,-1,-1):
            dp=[0]*(amount+1)
            dp[0]=1
            for target in range(amount+1):
                pick=0
                if coins[i]<=target:
                    pick=dp[target-coins[i]]
                notpick=prev[target]
                dp[target]=pick+notpick
            prev=dp[:]

        return prev[amount]             
```

---

[View on LeetCode](https://leetcode.com/problems/coin-change-ii/)