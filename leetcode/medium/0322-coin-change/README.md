# Coin Change

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given an integer array `coins` representing coins of different denominations and an integer `amount` representing a total amount of money.

Return the  **fewest**  number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Original
Python
 **Example 1:** 

```
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

```

 **Example 2:** 

```
Input: coins = [2], amount = 3
Output: -1

```

 **Example 3:** 

```
Input: coins = [1], amount = 0
Output: 0

```

 

 **Constraints:** 

- 1 <= coins.length <= 12
- 1 <= coins[i] <= 231 - 1
- 0 <= amount <= 104

## Solution

**Language:** Python  
**Runtime:** 2146 ms (beats 5.01%)  
**Memory:** 19.1 MB (beats 14.42%)  
**Submitted:** 2026-11-15T12:41:50.154Z  

```py
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        n=len(coins)
        def find(coins,amount,i,dp):
            
            if i==len(coins)-1:
                if amount%coins[i]==0:
                    return amount//coins[i]
                # else
                return float('inf')
            
            if coins[i]>amount:
                return find(coins,amount,i+1,dp)
            if dp[i][amount]!=-1:
                return dp[i][amount]
            pick=1+find(coins,amount-coins[i],i,dp)
            notpick=find(coins,amount,i+1,dp) 
            dp[i][amount]=min(pick,notpick)
            return min(pick,notpick)
        
        

        dp=[[-1]*(amount+1) for i in range(n)]
        ans = find(coins,amount,0,dp) 
        return ans if ans!=float('inf') else -1
        # for i in range(n-1,-1,-1):
        #     for target in range(1,amount+1):
        #         if target%coins[i]==0:
        #             dp[i][target]=target//coins[i]
        #         else:
            

```

---

[View on LeetCode](https://leetcode.com/problems/coin-change/)