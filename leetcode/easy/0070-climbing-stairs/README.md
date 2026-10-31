# Climbing Stairs

![Difficulty](https://img.shields.io/badge/Difficulty-Easy-green)

## Problem

You are climbing a staircase. It takes `n` steps to reach the top.

Each time you can either climb `1` or `2` steps. In how many distinct ways can you climb to the top?

 

 **Example 1:** 

```
Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

```

 **Example 2:** 

```
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

```

 

 **Constraints:** 

- 1 <= n <= 45

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 12.2 MB (beats 91.18%)  
**Submitted:** 2026-10-31T07:42:39.136Z  

```py
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[-1]*(n+1)
        dp[0]=1
        dp[1]=1
            
        for i in range(2,len(dp)):
            dp[i]= dp[i-1]+dp[i-2]
        return dp[n]
```

---

[View on LeetCode](https://leetcode.com/problems/climbing-stairs/)