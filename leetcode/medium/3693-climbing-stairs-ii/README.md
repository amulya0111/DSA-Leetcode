# Climbing Stairs II

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are climbing a staircase with `n + 1` steps, numbered from 0 to `n`.

You are also given a  **1-indexed**  integer array `costs` of length `n`, where `costs[i]` is the cost of step `i`.

From step `i`, you can jump  **only**  to step `i + 1`, `i + 2`, or `i + 3`. The cost of jumping from step `i` to step `j` is defined as: `costs[j] + (j - i)2`

You start from step 0 with `cost = 0`.

Return the  **minimum**  total cost to reach step `n`.

 

Original
Python
 **Example 1:** 

 **Input:**  n = 4, costs = [1,2,3,4]

 **Output:**  13

 **Explanation:** 

One optimal path is `0 → 1 → 2 → 4`

Jump	Cost Calculation	Cost
0 → 1	`costs[1] + (1 - 0)2 = 1 + 1`	2
1 → 2	`costs[2] + (2 - 1)2 = 2 + 1`	3
2 → 4	`costs[4] + (4 - 2)2 = 4 + 4`	8

Thus, the minimum total cost is `2 + 3 + 8 = 13`

 **Example 2:** 

 **Input:**  n = 4, costs = [5,1,6,2]

 **Output:**  11

 **Explanation:** 

One optimal path is `0 → 2 → 4`

Jump	Cost Calculation	Cost
0 → 2	`costs[2] + (2 - 0)2 = 1 + 4`	5
2 → 4	`costs[4] + (4 - 2)2 = 2 + 4`	6

Thus, the minimum total cost is `5 + 6 = 11`

 **Example 3:** 

 **Input:**  n = 3, costs = [9,8,3]

 **Output:**  12

 **Explanation:** 

The optimal path is `0 → 3` with total cost = `costs[3] + (3 - 0)2 = 3 + 9 = 12`

 

 **Constraints:** 

- 1 <= n == costs.length <= 105​​​​​​​
- 1 <= costs[i] <= 104

## Solution

**Language:** Python  
**Runtime:** 1276 ms (beats 12.73%)  
**Memory:** 23.5 MB (beats 74.55%)  
**Submitted:** 2026-11-10T18:18:47.274Z  

```py
class Solution(object):
    def climbStairs(self, n, costs):
        
        dp=[0]*(n+1)

        for i in range(n-1,-1,-1):
            ans=float('inf')

            for step in range(1,4):
                if i+step<=n:
                    jump=costs[i+step-1]+step**2
                    ans=min(ans,jump+dp[i+step])

            dp[i]=ans

        return dp[0]
```

---

[View on LeetCode](https://leetcode.com/problems/climbing-stairs-ii/)