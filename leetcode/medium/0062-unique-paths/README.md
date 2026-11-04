# Unique Paths

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

There is a robot on an `m x n` grid. The robot is initially located at the  **top-left corner**  (i.e., `grid[0][0]`). The robot tries to move to the  **bottom-right corner**  (i.e., `grid[m - 1][n - 1]`). The robot can only move either down or right at any point in time.

Given the two integers `m` and `n`, return  *the number of possible unique paths that the robot can take to reach the bottom-right corner*.

The test cases are generated so that the answer will be less than or equal to `2 * 109`.

 

 **Example 1:** 

```
Input: m = 3, n = 7
Output: 28

```

 **Example 2:** 

```
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

```

 

 **Constraints:** 

- 1 <= m, n <= 100

## Solution

**Language:** Python  
**Runtime:** 0 ms (beats 100.00%)  
**Memory:** 12.2 MB (beats 90.37%)  
**Submitted:** 2026-11-04T14:05:23.180Z  

```py
class Solution(object):
    def uniquePaths(self, m, n):
        # instead of pick and notpick , there will be right and down 
        dp=[1]*n
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                dp[j]=dp[j]+dp[j+1]
        return dp[0]

        # dp=[[1]*n for i in range(m)]
        # # for dp, change from bottom up to top down
        # for i in range(m-2,-1,-1):
        #     for j in range(n-2,-1,-1):
        #         dp[i][j]=dp[i][j+1]+dp[i+1][j]
        # return dp[0][0]


        # def countways(x,y,m,n):
        #     if x==m-1 and y==n-1:
        #         return 1
        #     elif x>=m or y>=n:
        #         return 0
        #     # right or down
        #     right = countways(x,y+1,m,n)
        #     down  = countways(x+1,y,m,n)
        #     return right + down
        # return countways(0,0,m,n)
```

---

[View on LeetCode](https://leetcode.com/problems/unique-paths/)